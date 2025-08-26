from aiogram import Bot
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.bot.models import ServicesContainer
from app.config import Config

from .invite_stats import InviteStatsService
from .notification import NotificationService
from .payment_stats import PaymentStatsService
from .plan import PlanService
from .referral import ReferralService
from .remnawave_server_pool import RemnavaveServerPoolService
from .subscription import SubscriptionService
from .remnawave_vpn import RemnavaveVPNService


async def initialize(
    config: Config,
    session: async_sessionmaker,
    bot: Bot,
) -> ServicesContainer:
    server_pool = RemnavaveServerPoolService(config=config, session=session)
    plan = PlanService()
    vpn = RemnavaveVPNService(config=config, session=session, server_pool_service=server_pool)
    notification = NotificationService(config=config, bot=bot)
    referral = ReferralService(config=config, session_factory=session, vpn_service=vpn)
    subscription = SubscriptionService(config=config, session_factory=session, vpn_service=vpn)
    payment_stats = PaymentStatsService(session_factory=session)
    invite_stats = InviteStatsService(session_factory=session, payment_stats_service=payment_stats)

    return ServicesContainer(
        server_pool=server_pool,
        plan=plan,
        vpn=vpn,
        notification=notification,
        referral=referral,
        subscription=subscription,
        payment_stats=payment_stats,
        invite_stats=invite_stats,
    )
