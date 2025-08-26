import logging
from dataclasses import dataclass
from typing import List, Optional

from sqlalchemy.ext.asyncio import async_sessionmaker

from app.bot.services.remnawave_api import RemnavaveApiClient, RemnavaveNode
from app.config import Config
from app.db.models import Server, User

logger = logging.getLogger(__name__)


@dataclass
class NodeConnection:
    node: RemnavaveNode
    api: RemnavaveApiClient


class RemnavaveServerPoolService:
    def __init__(self, config: Config, session: async_sessionmaker) -> None:
        self.config = config
        self.session = session
        self._nodes: dict[str, RemnavaveNode] = {}
        self._api_client: Optional[RemnavaveApiClient] = None
        logger.info("Remnawave Server Pool Service initialized.")

    async def _get_api_client(self) -> RemnavaveApiClient:
        """Get or create API client"""
        if not self._api_client:
            self._api_client = RemnavaveApiClient(
                base_url=self.config.remnavave.API_URL,
                username=self.config.remnavave.USERNAME,
                password=self.config.remnavave.PASSWORD
            )
            await self._api_client.login()
        return self._api_client

    async def sync_nodes(self) -> None:
        """Sync nodes from Remnawave API"""
        try:
            api = await self._get_api_client()
            nodes = await api.get_all_nodes()
            
            # Update internal cache
            self._nodes.clear()
            for node in nodes:
                if not node.is_disabled and node.is_node_online and node.is_xray_running:
                    self._nodes[node.uuid] = node
            
            logger.info(f"Synced {len(self._nodes)} active nodes from Remnawave")
            
            # Sync with database - update Server records to match Remnawave nodes
            await self._sync_with_database(nodes)
            
        except Exception as e:
            logger.error(f"Failed to sync nodes: {e}")

    async def _sync_with_database(self, nodes: List[RemnavaveNode]) -> None:
        """Sync nodes with database Server records"""
        async with self.session() as session:
            # Get existing servers from database
            db_servers = await Server.get_all(session)
            existing_server_map = {server.name: server for server in db_servers}
            
            for node in nodes:
                if node.name not in existing_server_map:
                    # Create new server record for this node
                    await Server.create(
                        session=session,
                        name=node.name,
                        host=node.address,
                        max_clients=1000,  # Default max clients for Remnawave nodes
                        location=node.country_code,
                        online=node.is_node_online and node.is_xray_running and not node.is_disabled
                    )
                    logger.info(f"Created server record for node {node.name}")
                else:
                    # Update existing server
                    server = existing_server_map[node.name]
                    await Server.update(
                        session=session,
                        name=node.name,
                        host=node.address,
                        location=node.country_code,
                        online=node.is_node_online and node.is_xray_running and not node.is_disabled
                    )

    async def get_available_nodes(self) -> List[RemnavaveNode]:
        """Get list of available nodes"""
        await self.sync_nodes()
        return [node for node in self._nodes.values() 
                if node.is_node_online and node.is_xray_running and not node.is_disabled]

    async def get_node_by_uuid(self, uuid: str) -> Optional[RemnavaveNode]:
        """Get node by UUID"""
        await self.sync_nodes()
        return self._nodes.get(uuid)

    async def get_best_node(self) -> Optional[RemnavaveNode]:
        """Get the best available node (least loaded)"""
        available_nodes = await self.get_available_nodes()
        
        if not available_nodes:
            logger.warning("No available nodes found")
            return None
        
        # For now, just return the first available node
        # In the future, we could implement load balancing based on user count or traffic
        best_node = available_nodes[0]
        logger.debug(f"Selected node: {best_node.name} ({best_node.address})")
        return best_node

    async def assign_server_to_user(self, user: User) -> Optional[RemnavaveNode]:
        """Assign a server/node to user - for Remnawave, this is less relevant since users are global"""
        # In Remnawave, users are managed globally, not per-node
        # But we can still assign a "preferred" node for database compatibility
        best_node = await self.get_best_node()
        
        if best_node:
            # Find corresponding server in database
            async with self.session() as session:
                server = await Server.get_by_name(session=session, name=best_node.name)
                if server:
                    await User.update(session=session, tg_id=user.tg_id, server_id=server.id)
                    logger.debug(f"Assigned server {server.name} to user {user.tg_id}")
        
        return best_node

    async def get_connection(self, user: User) -> Optional[NodeConnection]:
        """Get connection for user - in Remnawave, this returns the API client and best node"""
        # For Remnawave, we don't need per-node connections since it's centralized
        # But we maintain this interface for compatibility
        best_node = await self.get_best_node()
        
        if best_node:
            api = await self._get_api_client()
            return NodeConnection(node=best_node, api=api)
        
        return None

    async def refresh_node(self, node_name: str) -> None:
        """Refresh specific node information"""
        try:
            api = await self._get_api_client()
            nodes = await api.get_all_nodes()
            
            for node in nodes:
                if node.name == node_name:
                    if not node.is_disabled and node.is_node_online and node.is_xray_running:
                        self._nodes[node.uuid] = node
                    elif node.uuid in self._nodes:
                        del self._nodes[node.uuid]
                    
                    logger.info(f"Refreshed node {node_name}")
                    break
        except Exception as e:
            logger.error(f"Failed to refresh node {node_name}: {e}")

    async def get_node_stats(self) -> dict:
        """Get statistics about nodes"""
        await self.sync_nodes()
        
        total_nodes = len(self._nodes)
        online_nodes = sum(1 for node in self._nodes.values() 
                          if node.is_node_online and node.is_xray_running)
        
        return {
            "total_nodes": total_nodes,
            "online_nodes": online_nodes,
            "offline_nodes": total_nodes - online_nodes
        }

    async def close(self) -> None:
        """Close API client connections"""
        if self._api_client:
            await self._api_client.client.aclose()
            self._api_client = None