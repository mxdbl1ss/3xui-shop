POST
/api/admin/token
Admin Token

Authenticate an admin and issue a token.

Parameters
Try it out
No parameters

Request body

application/x-www-form-urlencoded
grant*type
string | (string | null)
pattern: password
username *
string
password \_
string
scope
string
client_id
string | (string | null)
client_secret
string | (string | null)
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"access_token": "string",
"token_type": "bearer"
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

GET
/api/admin
Get Current Admin

Retrieve the current authenticated admin.

Parameters
Try it out
No parameters

Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"username": "string",
"is_sudo": true,
"telegram_id": 0,
"discord_webhook": "string",
"users_usage": 0
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links

POST
/api/admin
Create Admin

Create a new admin if the current admin has sudo privileges.

Parameters
Try it out
No parameters

Request body

application/json
Example Value
Schema
{
"username": "string",
"is_sudo": true,
"telegram_id": 0,
"discord_webhook": "string",
"users_usage": 0,
"password": "string"
}
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"username": "string",
"is_sudo": true,
"telegram_id": 0,
"discord_webhook": "string",
"users_usage": 0
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
409
Conflict

Media type

application/json
Example Value
Schema
{
"detail": "Entity already exists"
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

PUT
/api/admin/{username}
Modify Admin

Modify an existing admin's details.

Parameters
Try it out
Name Description
username \*
string
(path)
username
Request body

application/json
Example Value
Schema
{
"password": "string",
"is_sudo": true,
"telegram_id": 0,
"discord_webhook": "string"
}
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"username": "string",
"is_sudo": true,
"telegram_id": 0,
"discord_webhook": "string",
"users_usage": 0
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

DELETE
/api/admin/{username}
Remove Admin

Remove an admin from the database.

Parameters
Try it out
Name Description
username \*
string
(path)
username
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
"string"
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

GET
/api/admins
Get Admins

Fetch a list of admins with optional filters for pagination and username.

Parameters
Try it out
Name Description
offset
integer | (integer | null)
(query)
offset
limit
integer | (integer | null)
(query)
limit
username
string | (string | null)
(query)
username
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
[
{
"username": "string",
"is_sudo": true,
"telegram_id": 0,
"discord_webhook": "string",
"users_usage": 0
}
]
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

POST
/api/admin/{username}/users/disable
Disable All Active Users

Disable all active users under a specific admin

Parameters
Try it out
Name Description
username \*
string
(path)
username
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
"string"
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
404
Not found

Media type

application/json
Example Value
Schema
{
"detail": "Entity {} not found"
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

POST
/api/admin/{username}/users/activate
Activate All Disabled Users

Activate all disabled users under a specific admin

Parameters
Try it out
Name Description
username \*
string
(path)
username
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
"string"
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
404
Not found

Media type

application/json
Example Value
Schema
{
"detail": "Entity {} not found"
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

POST
/api/admin/usage/reset/{username}
Reset Admin Usage

Resets usage of admin.

Parameters
Try it out
Name Description
username \*
string
(path)
username
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"username": "string",
"is_sudo": true,
"telegram_id": 0,
"discord_webhook": "string",
"users_usage": 0
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

GET
/api/admin/usage/{username}
Get Admin Usage

Retrieve the usage of given admin.

Parameters
Try it out
Name Description
username \*
string
(path)
username
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
0
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links
Core

GET
/api/core
Get Core Stats

Retrieve core statistics such as version and uptime.

Parameters
Try it out
No parameters

Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"version": "string",
"started": true,
"logs_websocket": "string"
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links

POST
/api/core/restart
Restart Core

Restart the core and all connected nodes.

Parameters
Try it out
No parameters

Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
"string"
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links

GET
/api/core/config
Get Core Config

Get the current core configuration.

Parameters
Try it out
No parameters

Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links

PUT
/api/core/config
Modify Core Config

Modify the core configuration and restart the core.

Parameters
Try it out
No parameters

Request body

application/json
Example Value
Schema
{}
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links
Node

GET
/api/node/settings
Get Node Settings

Retrieve the current node settings, including TLS certificate.

Parameters
Try it out
No parameters

Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"min_node_version": "v0.2.0",
"certificate": "string"
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links

POST
/api/node
Add Node

Add a new node to the database and optionally add it as a host.

Parameters
Try it out
No parameters

Request body

application/json
Example Value
Schema
{
"add_as_new_host": true,
"address": "192.168.1.1",
"api_port": 62051,
"name": "DE node",
"port": 62050,
"usage_coefficient": 1
}
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"name": "string",
"address": "string",
"port": 62050,
"api_port": 62051,
"usage_coefficient": 1,
"id": 0,
"xray_version": "string",
"status": "connected",
"message": "string"
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
409
Conflict

Media type

application/json
Example Value
Schema
{
"detail": "Entity already exists"
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

GET
/api/node/{node_id}
Get Node

Retrieve details of a specific node by its ID.

Parameters
Try it out
Name Description
node_id \*
integer
(path)
node_id
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"name": "string",
"address": "string",
"port": 62050,
"api_port": 62051,
"usage_coefficient": 1,
"id": 0,
"xray_version": "string",
"status": "connected",
"message": "string"
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

PUT
/api/node/{node_id}
Modify Node

Update a node's details. Only accessible to sudo admins.

Parameters
Try it out
Name Description
node_id \*
integer
(path)
node_id
Request body

application/json
Example Value
Schema
{
"address": "192.168.1.1",
"api_port": 62051,
"name": "DE node",
"port": 62050,
"status": "disabled",
"usage_coefficient": 1
}
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"name": "string",
"address": "string",
"port": 62050,
"api_port": 62051,
"usage_coefficient": 1,
"id": 0,
"xray_version": "string",
"status": "connected",
"message": "string"
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

DELETE
/api/node/{node_id}
Remove Node

Delete a node and remove it from xray in the background.

Parameters
Try it out
Name Description
node_id \*
integer
(path)
node_id
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
"string"
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

GET
/api/nodes
Get Nodes

Retrieve a list of all nodes. Accessible only to sudo admins.

Parameters
Try it out
No parameters

Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
[
{
"name": "string",
"address": "string",
"port": 62050,
"api_port": 62051,
"usage_coefficient": 1,
"id": 0,
"xray_version": "string",
"status": "connected",
"message": "string"
}
]
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links

POST
/api/node/{node_id}/reconnect
Reconnect Node

Trigger a reconnection for the specified node. Only accessible to sudo admins.

Parameters
Try it out
Name Description
node_id \*
integer
(path)
node_id
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
"string"
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

GET
/api/nodes/usage
Get Usage

Retrieve usage statistics for nodes within a specified date range.

Parameters
Try it out
Name Description
start
string
(query)
Default value :

start
end
string
(query)
Default value :

end
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"usages": [
{
"node_id": 0,
"node_name": "string",
"uplink": 0,
"downlink": 0
}
]
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links
Subscription

GET
/sub/{token}/
User Subscription

Provides a subscription link based on the user agent (Clash, V2Ray, etc.).

Parameters
Try it out
Name Description
token \*
string
(path)
token
user-agent
string
(header)
Default value :

user-agent
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
"string"
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

GET
/sub/{token}/info
User Subscription Info

Retrieves detailed information about the user's subscription.

Parameters
Try it out
Name Description
token \*
string
(path)
token
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"proxies": {},
"expire": 0,
"data_limit": 0,
"data_limit_reset_strategy": "no_reset",
"sub_updated_at": "2025-08-22T14:24:16.670Z",
"sub_last_user_agent": "string",
"online_at": "2025-08-22T14:24:16.670Z",
"on_hold_expire_duration": 0,
"on_hold_timeout": "2025-08-22T14:24:16.670Z",
"next_plan": {
"data_limit": 0,
"expire": 0,
"add_remaining_traffic": false,
"fire_on_either": true
},
"username": "string",
"status": "active",
"used_traffic": 0,
"lifetime_used_traffic": 0,
"created_at": "2025-08-22T14:24:16.670Z",
"links": [],
"subscription_url": ""
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

GET
/sub/{token}/usage
User Get Usage

Fetches the usage statistics for the user within a specified date range.

Parameters
Try it out
Name Description
token \*
string
(path)
token
start
string
(query)
Default value :

start
end
string
(query)
Default value :

end
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
"string"
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

GET
/sub/{token}/{client_type}
User Subscription With Client Type

Provides a subscription link based on the specified client type (e.g., Clash, V2Ray).

Parameters
Try it out
Name Description
client*type *
string
(path)
client*type
pattern: sing-box|clash-meta|clash|outline|v2ray|v2ray-json
token *
string
(path)
token
user-agent
string
(header)
Default value :

user-agent
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
"string"
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links
System

GET
/api/system
Get System Stats

Fetch system stats including memory, CPU, and user metrics.

Parameters
Try it out
No parameters

Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"version": "string",
"mem_total": 0,
"mem_used": 0,
"cpu_cores": 0,
"cpu_usage": 0,
"total_user": 0,
"online_users": 0,
"users_active": 0,
"users_on_hold": 0,
"users_disabled": 0,
"users_expired": 0,
"users_limited": 0,
"incoming_bandwidth": 0,
"outgoing_bandwidth": 0,
"incoming_bandwidth_speed": 0,
"outgoing_bandwidth_speed": 0
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links

GET
/api/inbounds
Get Inbounds

Retrieve inbound configurations grouped by protocol.

Parameters
Try it out
No parameters

Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"additionalProp1": [
{
"tag": "string",
"protocol": "vmess",
"network": "string",
"tls": "string",
"port": 0
}
],
"additionalProp2": [
{
"tag": "string",
"protocol": "vmess",
"network": "string",
"tls": "string",
"port": 0
}
],
"additionalProp3": [
{
"tag": "string",
"protocol": "vmess",
"network": "string",
"tls": "string",
"port": 0
}
]
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links

GET
/api/hosts
Get Hosts

Get a list of proxy hosts grouped by inbound tag.

Parameters
Try it out
No parameters

Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"additionalProp1": [
{
"remark": "string",
"address": "string",
"port": 0,
"sni": "string",
"host": "string",
"path": "string",
"security": "inbound_default",
"alpn": "",
"fingerprint": "",
"allowinsecure": true,
"is_disabled": true,
"mux_enable": true,
"fragment_setting": "string",
"noise_setting": "string",
"random_user_agent": true,
"use_sni_as_host": true
}
],
"additionalProp2": [
{
"remark": "string",
"address": "string",
"port": 0,
"sni": "string",
"host": "string",
"path": "string",
"security": "inbound_default",
"alpn": "",
"fingerprint": "",
"allowinsecure": true,
"is_disabled": true,
"mux_enable": true,
"fragment_setting": "string",
"noise_setting": "string",
"random_user_agent": true,
"use_sni_as_host": true
}
],
"additionalProp3": [
{
"remark": "string",
"address": "string",
"port": 0,
"sni": "string",
"host": "string",
"path": "string",
"security": "inbound_default",
"alpn": "",
"fingerprint": "",
"allowinsecure": true,
"is_disabled": true,
"mux_enable": true,
"fragment_setting": "string",
"noise_setting": "string",
"random_user_agent": true,
"use_sni_as_host": true
}
]
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links

PUT
/api/hosts
Modify Hosts

Modify proxy hosts and update the configuration.

Parameters
Try it out
No parameters

Request body

application/json
Example Value
Schema
{
"additionalProp1": [
{
"remark": "string",
"address": "string",
"port": 0,
"sni": "string",
"host": "string",
"path": "string",
"security": "inbound_default",
"alpn": "",
"fingerprint": "",
"allowinsecure": true,
"is_disabled": true,
"mux_enable": true,
"fragment_setting": "string",
"noise_setting": "string",
"random_user_agent": true,
"use_sni_as_host": true
}
],
"additionalProp2": [
{
"remark": "string",
"address": "string",
"port": 0,
"sni": "string",
"host": "string",
"path": "string",
"security": "inbound_default",
"alpn": "",
"fingerprint": "",
"allowinsecure": true,
"is_disabled": true,
"mux_enable": true,
"fragment_setting": "string",
"noise_setting": "string",
"random_user_agent": true,
"use_sni_as_host": true
}
],
"additionalProp3": [
{
"remark": "string",
"address": "string",
"port": 0,
"sni": "string",
"host": "string",
"path": "string",
"security": "inbound_default",
"alpn": "",
"fingerprint": "",
"allowinsecure": true,
"is_disabled": true,
"mux_enable": true,
"fragment_setting": "string",
"noise_setting": "string",
"random_user_agent": true,
"use_sni_as_host": true
}
]
}
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"additionalProp1": [
{
"remark": "string",
"address": "string",
"port": 0,
"sni": "string",
"host": "string",
"path": "string",
"security": "inbound_default",
"alpn": "",
"fingerprint": "",
"allowinsecure": true,
"is_disabled": true,
"mux_enable": true,
"fragment_setting": "string",
"noise_setting": "string",
"random_user_agent": true,
"use_sni_as_host": true
}
],
"additionalProp2": [
{
"remark": "string",
"address": "string",
"port": 0,
"sni": "string",
"host": "string",
"path": "string",
"security": "inbound_default",
"alpn": "",
"fingerprint": "",
"allowinsecure": true,
"is_disabled": true,
"mux_enable": true,
"fragment_setting": "string",
"noise_setting": "string",
"random_user_agent": true,
"use_sni_as_host": true
}
],
"additionalProp3": [
{
"remark": "string",
"address": "string",
"port": 0,
"sni": "string",
"host": "string",
"path": "string",
"security": "inbound_default",
"alpn": "",
"fingerprint": "",
"allowinsecure": true,
"is_disabled": true,
"mux_enable": true,
"fragment_setting": "string",
"noise_setting": "string",
"random_user_agent": true,
"use_sni_as_host": true
}
]
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links
User Template

POST
/api/user_template
Add User Template

Add a new user template

name can be up to 64 characters
data_limit must be in bytes and larger or equal to 0
expire_duration must be in seconds and larger or equat to 0
inbounds dictionary of protocol:inbound_tags, empty means all inbounds
Parameters
Try it out
No parameters

Request body

application/json
Example Value
Schema
{
"data_limit": 0,
"expire_duration": 0,
"inbounds": {
"vless": [
"VLESS_INBOUND"
],
"vmess": [
"VMESS_INBOUND"
]
},
"name": "my template 1"
}
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"name": "string",
"data_limit": 0,
"expire_duration": 0,
"username_prefix": "string",
"username_suffix": "string",
"inbounds": {},
"id": 0
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

GET
/api/user_template
Get User Templates

Get a list of User Templates with optional pagination

Parameters
Try it out
Name Description
offset
integer
(query)
offset
limit
integer
(query)
limit
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
[
{
"name": "string",
"data_limit": 0,
"expire_duration": 0,
"username_prefix": "string",
"username_suffix": "string",
"inbounds": {},
"id": 0
}
]
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

GET
/api/user_template/{template_id}
Get User Template Endpoint

Get User Template information with id

Parameters
Try it out
Name Description
template_id \*
integer
(path)
template_id
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"name": "string",
"data_limit": 0,
"expire_duration": 0,
"username_prefix": "string",
"username_suffix": "string",
"inbounds": {},
"id": 0
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

PUT
/api/user_template/{template_id}
Modify User Template

Modify User Template

name can be up to 64 characters
data_limit must be in bytes and larger or equal to 0
expire_duration must be in seconds and larger or equat to 0
inbounds dictionary of protocol:inbound_tags, empty means all inbounds
Parameters
Try it out
Name Description
template_id \*
integer
(path)
template_id
Request body

application/json
Example Value
Schema
{
"data_limit": 0,
"expire_duration": 0,
"inbounds": {
"vless": [
"VLESS_INBOUND"
],
"vmess": [
"VMESS_INBOUND"
]
},
"name": "my template 1"
}
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"name": "string",
"data_limit": 0,
"expire_duration": 0,
"username_prefix": "string",
"username_suffix": "string",
"inbounds": {},
"id": 0
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

DELETE
/api/user_template/{template_id}
Remove User Template

Remove a User Template by its ID

Parameters
Try it out
Name Description
template_id \*
integer
(path)
template_id
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
"string"
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links
User

POST
/api/user
Add User

Add a new user

username: 3 to 32 characters, can include a-z, 0-9, and underscores.
status: User's status, defaults to active. Special rules if on_hold.
expire: UTC timestamp for account expiration. Use 0 for unlimited.
data_limit: Max data usage in bytes (e.g., 1073741824 for 1GB). 0 means unlimited.
data_limit_reset_strategy: Defines how/if data limit resets. no_reset means it never resets.
proxies: Dictionary of protocol settings (e.g., vmess, vless).
inbounds: Dictionary of protocol tags to specify inbound connections.
note: Optional text field for additional user information or notes.
on_hold_timeout: UTC timestamp when on_hold status should start or end.
on_hold_expire_duration: Duration (in seconds) for how long the user should stay in on_hold status.
next_plan: Next user plan (resets after use).
Parameters
Try it out
No parameters

Request body

application/json
Example Value
Schema
{
"data_limit": 0,
"data_limit_reset_strategy": "no_reset",
"expire": 0,
"inbounds": {
"vless": [
"VLESS TCP REALITY",
"VLESS GRPC REALITY"
],
"vmess": [
"VMess TCP",
"VMess Websocket"
]
},
"next_plan": {
"add_remaining_traffic": false,
"data_limit": 0,
"expire": 0,
"fire_on_either": true
},
"note": "",
"on_hold_expire_duration": 0,
"on_hold_timeout": "2023-11-03T20:30:00",
"proxies": {
"vless": {},
"vmess": {
"id": "35e4e39c-7d5c-4f4b-8b71-558e4f37ff53"
}
},
"status": "active",
"username": "user1234"
}
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"proxies": {},
"expire": 0,
"data_limit": 0,
"data_limit_reset_strategy": "no_reset",
"inbounds": {},
"note": "string",
"sub_updated_at": "2025-08-22T14:24:16.707Z",
"sub_last_user_agent": "string",
"online_at": "2025-08-22T14:24:16.707Z",
"on_hold_expire_duration": 0,
"on_hold_timeout": "2025-08-22T14:24:16.707Z",
"auto_delete_in_days": 0,
"next_plan": {
"data_limit": 0,
"expire": 0,
"add_remaining_traffic": false,
"fire_on_either": true
},
"username": "string",
"status": "active",
"used_traffic": 0,
"lifetime_used_traffic": 0,
"created_at": "2025-08-22T14:24:16.707Z",
"links": [],
"subscription_url": "",
"excluded_inbounds": {},
"admin": {
"username": "string",
"is_sudo": true,
"telegram_id": 0,
"discord_webhook": "string",
"users_usage": 0
}
}
No links
400
Bad request

Media type

application/json
Example Value
Schema
{
"detail": "string"
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
409
Conflict

Media type

application/json
Example Value
Schema
{
"detail": "Entity already exists"
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

GET
/api/user/{username}
Get User

Get user information

Parameters
Try it out
Name Description
username \*
string
(path)
username
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"proxies": {},
"expire": 0,
"data_limit": 0,
"data_limit_reset_strategy": "no_reset",
"inbounds": {},
"note": "string",
"sub_updated_at": "2025-08-22T14:24:16.716Z",
"sub_last_user_agent": "string",
"online_at": "2025-08-22T14:24:16.716Z",
"on_hold_expire_duration": 0,
"on_hold_timeout": "2025-08-22T14:24:16.716Z",
"auto_delete_in_days": 0,
"next_plan": {
"data_limit": 0,
"expire": 0,
"add_remaining_traffic": false,
"fire_on_either": true
},
"username": "string",
"status": "active",
"used_traffic": 0,
"lifetime_used_traffic": 0,
"created_at": "2025-08-22T14:24:16.717Z",
"links": [],
"subscription_url": "",
"excluded_inbounds": {},
"admin": {
"username": "string",
"is_sudo": true,
"telegram_id": 0,
"discord_webhook": "string",
"users_usage": 0
}
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
404
Not found

Media type

application/json
Example Value
Schema
{
"detail": "Entity {} not found"
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

PUT
/api/user/{username}
Modify User

Modify an existing user

username: Cannot be changed. Used to identify the user.
status: User's new status. Can be 'active', 'disabled', 'on_hold', 'limited', or 'expired'.
expire: UTC timestamp for new account expiration. Set to 0 for unlimited, null for no change.
data_limit: New max data usage in bytes (e.g., 1073741824 for 1GB). Set to 0 for unlimited, null for no change.
data_limit_reset_strategy: New strategy for data limit reset. Options include 'daily', 'weekly', 'monthly', or 'no_reset'.
proxies: Dictionary of new protocol settings (e.g., vmess, vless). Empty dictionary means no change.
inbounds: Dictionary of new protocol tags to specify inbound connections. Empty dictionary means no change.
note: New optional text for additional user information or notes. null means no change.
on_hold_timeout: New UTC timestamp for when on_hold status should start or end. Only applicable if status is changed to 'on_hold'.
on_hold_expire_duration: New duration (in seconds) for how long the user should stay in on_hold status. Only applicable if status is changed to 'on_hold'.
next_plan: Next user plan (resets after use).
Note: Fields set to null or omitted will not be modified.

Parameters
Try it out
Name Description
username \*
string
(path)
username
Request body

application/json
Example Value
Schema
{
"data_limit": 0,
"data_limit_reset_strategy": "no_reset",
"expire": 0,
"inbounds": {
"vless": [
"VLESS TCP REALITY",
"VLESS GRPC REALITY"
],
"vmess": [
"VMess TCP",
"VMess Websocket"
]
},
"next_plan": {
"add_remaining_traffic": false,
"data_limit": 0,
"expire": 0,
"fire_on_either": true
},
"note": "",
"on_hold_expire_duration": 0,
"on_hold_timeout": "2023-11-03T20:30:00",
"proxies": {
"vless": {},
"vmess": {
"id": "35e4e39c-7d5c-4f4b-8b71-558e4f37ff53"
}
},
"status": "active"
}
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"proxies": {},
"expire": 0,
"data_limit": 0,
"data_limit_reset_strategy": "no_reset",
"inbounds": {},
"note": "string",
"sub_updated_at": "2025-08-22T14:24:16.724Z",
"sub_last_user_agent": "string",
"online_at": "2025-08-22T14:24:16.724Z",
"on_hold_expire_duration": 0,
"on_hold_timeout": "2025-08-22T14:24:16.724Z",
"auto_delete_in_days": 0,
"next_plan": {
"data_limit": 0,
"expire": 0,
"add_remaining_traffic": false,
"fire_on_either": true
},
"username": "string",
"status": "active",
"used_traffic": 0,
"lifetime_used_traffic": 0,
"created_at": "2025-08-22T14:24:16.724Z",
"links": [],
"subscription_url": "",
"excluded_inbounds": {},
"admin": {
"username": "string",
"is_sudo": true,
"telegram_id": 0,
"discord_webhook": "string",
"users_usage": 0
}
}
No links
400
Bad request

Media type

application/json
Example Value
Schema
{
"detail": "string"
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
404
Not found

Media type

application/json
Example Value
Schema
{
"detail": "Entity {} not found"
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

DELETE
/api/user/{username}
Remove User

Remove a user

Parameters
Try it out
Name Description
username \*
string
(path)
username
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
"string"
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
404
Not found

Media type

application/json
Example Value
Schema
{
"detail": "Entity {} not found"
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

POST
/api/user/{username}/reset
Reset User Data Usage

Reset user data usage

Parameters
Try it out
Name Description
username \*
string
(path)
username
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"proxies": {},
"expire": 0,
"data_limit": 0,
"data_limit_reset_strategy": "no_reset",
"inbounds": {},
"note": "string",
"sub_updated_at": "2025-08-22T14:24:16.734Z",
"sub_last_user_agent": "string",
"online_at": "2025-08-22T14:24:16.734Z",
"on_hold_expire_duration": 0,
"on_hold_timeout": "2025-08-22T14:24:16.734Z",
"auto_delete_in_days": 0,
"next_plan": {
"data_limit": 0,
"expire": 0,
"add_remaining_traffic": false,
"fire_on_either": true
},
"username": "string",
"status": "active",
"used_traffic": 0,
"lifetime_used_traffic": 0,
"created_at": "2025-08-22T14:24:16.734Z",
"links": [],
"subscription_url": "",
"excluded_inbounds": {},
"admin": {
"username": "string",
"is_sudo": true,
"telegram_id": 0,
"discord_webhook": "string",
"users_usage": 0
}
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
404
Not found

Media type

application/json
Example Value
Schema
{
"detail": "Entity {} not found"
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

POST
/api/user/{username}/revoke_sub
Revoke User Subscription

Revoke users subscription (Subscription link and proxies)

Parameters
Try it out
Name Description
username \*
string
(path)
username
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"proxies": {},
"expire": 0,
"data_limit": 0,
"data_limit_reset_strategy": "no_reset",
"inbounds": {},
"note": "string",
"sub_updated_at": "2025-08-22T14:24:16.739Z",
"sub_last_user_agent": "string",
"online_at": "2025-08-22T14:24:16.739Z",
"on_hold_expire_duration": 0,
"on_hold_timeout": "2025-08-22T14:24:16.739Z",
"auto_delete_in_days": 0,
"next_plan": {
"data_limit": 0,
"expire": 0,
"add_remaining_traffic": false,
"fire_on_either": true
},
"username": "string",
"status": "active",
"used_traffic": 0,
"lifetime_used_traffic": 0,
"created_at": "2025-08-22T14:24:16.739Z",
"links": [],
"subscription_url": "",
"excluded_inbounds": {},
"admin": {
"username": "string",
"is_sudo": true,
"telegram_id": 0,
"discord_webhook": "string",
"users_usage": 0
}
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
404
Not found

Media type

application/json
Example Value
Schema
{
"detail": "Entity {} not found"
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

GET
/api/users
Get Users

Get all users

Parameters
Try it out
Name Description
offset
integer
(query)
offset
limit
integer
(query)
limit
username
array<string>
(query)
search
string | (string | null)
(query)
search
admin
array<string> | (array<string> | null)
(query)
status
string
(query)
Available values : active, disabled, limited, expired, on_hold

--
sort
string
(query)
sort
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"users": [
{
"proxies": {},
"expire": 0,
"data_limit": 0,
"data_limit_reset_strategy": "no_reset",
"inbounds": {},
"note": "string",
"sub_updated_at": "2025-08-22T14:24:16.749Z",
"sub_last_user_agent": "string",
"online_at": "2025-08-22T14:24:16.749Z",
"on_hold_expire_duration": 0,
"on_hold_timeout": "2025-08-22T14:24:16.749Z",
"auto_delete_in_days": 0,
"next_plan": {
"data_limit": 0,
"expire": 0,
"add_remaining_traffic": false,
"fire_on_either": true
},
"username": "string",
"status": "active",
"used_traffic": 0,
"lifetime_used_traffic": 0,
"created_at": "2025-08-22T14:24:16.749Z",
"links": [],
"subscription_url": "",
"excluded_inbounds": {},
"admin": {
"username": "string",
"is_sudo": true,
"telegram_id": 0,
"discord_webhook": "string",
"users_usage": 0
}
}
],
"total": 0
}
No links
400
Bad request

Media type

application/json
Example Value
Schema
{
"detail": "string"
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
404
Not found

Media type

application/json
Example Value
Schema
{
"detail": "Entity {} not found"
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

POST
/api/users/reset
Reset Users Data Usage

Reset all users data usage

Parameters
Try it out
No parameters

Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
"string"
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
404
Not found

Media type

application/json
Example Value
Schema
{
"detail": "Entity {} not found"
}
No links

GET
/api/user/{username}/usage
Get User Usage

Get users usage

Parameters
Try it out
Name Description
username \*
string
(path)
username
start
string
(query)
Default value :

start
end
string
(query)
Default value :

end
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"username": "string",
"usages": [
{
"node_id": 0,
"node_name": "string",
"used_traffic": 0
}
]
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
404
Not found

Media type

application/json
Example Value
Schema
{
"detail": "Entity {} not found"
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

POST
/api/user/{username}/active-next
Active Next Plan

Reset user by next plan

Parameters
Try it out
Name Description
username \*
string
(path)
username
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"proxies": {},
"expire": 0,
"data_limit": 0,
"data_limit_reset_strategy": "no_reset",
"inbounds": {},
"note": "string",
"sub_updated_at": "2025-08-22T14:24:16.763Z",
"sub_last_user_agent": "string",
"online_at": "2025-08-22T14:24:16.763Z",
"on_hold_expire_duration": 0,
"on_hold_timeout": "2025-08-22T14:24:16.763Z",
"auto_delete_in_days": 0,
"next_plan": {
"data_limit": 0,
"expire": 0,
"add_remaining_traffic": false,
"fire_on_either": true
},
"username": "string",
"status": "active",
"used_traffic": 0,
"lifetime_used_traffic": 0,
"created_at": "2025-08-22T14:24:16.763Z",
"links": [],
"subscription_url": "",
"excluded_inbounds": {},
"admin": {
"username": "string",
"is_sudo": true,
"telegram_id": 0,
"discord_webhook": "string",
"users_usage": 0
}
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
403
Forbidden

Media type

application/json
Example Value
Schema
{
"detail": "You are not allowed to ..."
}
No links
404
Not found

Media type

application/json
Example Value
Schema
{
"detail": "Entity {} not found"
}
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

GET
/api/users/usage
Get Users Usage

Get all users usage

Parameters
Try it out
Name Description
start
string
(query)
Default value :

start
end
string
(query)
Default value :

end
admin
array<string> | (array<string> | null)
(query)
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"usages": [
{
"node_id": 0,
"node_name": "string",
"used_traffic": 0
}
]
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

PUT
/api/user/{username}/set-owner
Set Owner

Set a new owner (admin) for a user.

Parameters
Try it out
Name Description
username _
string
(path)
username
admin_username _
string
(query)
admin_username
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
{
"proxies": {},
"expire": 0,
"data_limit": 0,
"data_limit_reset_strategy": "no_reset",
"inbounds": {},
"note": "string",
"sub_updated_at": "2025-08-22T14:24:16.773Z",
"sub_last_user_agent": "string",
"online_at": "2025-08-22T14:24:16.773Z",
"on_hold_expire_duration": 0,
"on_hold_timeout": "2025-08-22T14:24:16.773Z",
"auto_delete_in_days": 0,
"next_plan": {
"data_limit": 0,
"expire": 0,
"add_remaining_traffic": false,
"fire_on_either": true
},
"username": "string",
"status": "active",
"used_traffic": 0,
"lifetime_used_traffic": 0,
"created_at": "2025-08-22T14:24:16.773Z",
"links": [],
"subscription_url": "",
"excluded_inbounds": {},
"admin": {
"username": "string",
"is_sudo": true,
"telegram_id": 0,
"discord_webhook": "string",
"users_usage": 0
}
}
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

GET
/api/users/expired
Get Expired Users

Get users who have expired within the specified date range.

expired_after UTC datetime (optional)
expired_before UTC datetime (optional)
At least one of expired_after or expired_before must be provided for filtering
If both are omitted, returns all expired users
Parameters
Try it out
Name Description
expired_after
string | (string | null)($date-time)
(query)
Example : 2024-01-01T00:00:00

2024-01-01T00:00:00
expired_before
string | (string | null)($date-time)
(query)
Example : 2024-01-31T23:59:59

2024-01-31T23:59:59
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
[
"string"
]
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links

DELETE
/api/users/expired
Delete Expired Users

Delete users who have expired within the specified date range.

expired_after UTC datetime (optional)
expired_before UTC datetime (optional)
At least one of expired_after or expired_before must be provided
Parameters
Try it out
Name Description
expired_after
string | (string | null)($date-time)
(query)
Example : 2024-01-01T00:00:00

2024-01-01T00:00:00
expired_before
string | (string | null)($date-time)
(query)
Example : 2024-01-31T23:59:59

2024-01-31T23:59:59
Responses
Code Description Links
200
Successful Response

Media type

application/json
Controls Accept header.
Example Value
Schema
[
"string"
]
No links
401
Unauthorized

Media type

application/json
Example Value
Schema
{
"detail": "Not authenticated"
}
Headers:
Name Description Type
WWW-Authenticate
Authentication type

string
No links
422
Validation Error

Media type

application/json
Example Value
Schema
{
"detail": [
{
"loc": [
"string",
0
],
"msg": "string",
"type": "string"
}
]
}
No links
default

GET
/
Base

Schemas
AdminCollapse allobject
usernamestring
is_sudoboolean
telegram_idCollapse all(integer | null)
Any ofCollapse all(integer | null)
#0integer
#1null
discord_webhookCollapse all(string | null)
Any ofCollapse all(string | null)
#0string
#1null
users_usageCollapse all(integer | null)
Any ofCollapse all(integer | null)
#0integer
#1null
AdminCreateCollapse allobject
usernamestring
is_sudoboolean
telegram_idExpand all(integer | null)
discord_webhookExpand all(string | null)
users_usageExpand all(integer | null)
passwordstring
AdminModifyCollapse allobject
passwordExpand all(string | null)
is_sudoboolean
telegram_idExpand all(integer | null)
discord_webhookExpand all(string | null)
Body_admin_token_api_admin_token_postCollapse allobject
grant_typeExpand all(string | null)
usernamestring
passwordstring
scopeExpand allstring
client_idExpand all(string | null)
client_secretExpand all(string | null)
ConflictCollapse allobject
detailExpand allstring
CoreStatsCollapse allobject
versionstring
startedboolean
logs_websocketstring
ForbiddenCollapse allobject
detailExpand allstring
HTTPExceptionCollapse allobject
detailstring
HTTPValidationErrorCollapse allobject
detailExpand allarray<object>
NextPlanModelCollapse allobject
data_limitExpand all(integer | null)
expireExpand all(integer | null)
add_remaining_trafficExpand allboolean
fire_on_eitherExpand allboolean
NodeCreateCollapse allobject
namestring
addressstring
portExpand allinteger
api_portExpand allinteger
usage_coefficientExpand allnumber> 0
add_as_new_hostExpand allboolean
ExampleExpand allobject
NodeModifyCollapse allobject
nameExpand all(string | null)
addressExpand all(string | null)
portExpand all(integer | null)
api_portExpand all(integer | null)
usage_coefficientExpand all(number | null)
statusExpand all(string | null)
ExampleExpand allobject
NodeResponseCollapse allobject
namestring
addressstring
portExpand allinteger
api_portExpand allinteger
usage_coefficientExpand allnumber> 0
idinteger
xray_versionExpand all(string | null)
statusExpand allstring
messageExpand all(string | null)
NodeSettingsCollapse allobject
min_node_versionExpand allstring
certificatestring
NodeStatusCollapse allstring
EnumExpand allarray
NodeUsageResponseCollapse allobject
node_idExpand all(integer | null)
node_namestring
uplinkinteger
downlinkinteger
NodesUsageResponseCollapse allobject
usagesExpand allarray<object>
NotFoundCollapse allobject
detailExpand allstring
ProxyHostCollapse allobject
remarkstring
addressstring
portExpand all(integer | null)
sniExpand all(string | null)
hostExpand all(string | null)
pathExpand all(string | null)
securityExpand allstring
alpnExpand allstring
fingerprintExpand allstring
allowinsecureExpand all(boolean | null)
is_disabledExpand all(boolean | null)
mux_enableExpand all(boolean | null)
fragment_settingExpand all(string | null)
noise_settingExpand all(string | null)
random_user_agentExpand all(boolean | null)
use_sni_as_hostExpand all(boolean | null)
ProxyHostALPNCollapse allstring
EnumExpand allarray
ProxyHostFingerprintCollapse allstring
EnumExpand allarray
ProxyHostSecurityCollapse allstring
EnumExpand allarray
ProxyInboundCollapse allobject
tagstring
protocolExpand allstring
networkstring
tlsstring
portExpand all(integer | string)
ProxySettingsCollapse allobject
ProxyTypesCollapse allstring
EnumExpand allarray
SubscriptionUserResponseCollapse allobject
proxiesobject
expireExpand all(integer | null)
data_limitExpand all(integer | null)
data_limit_reset_strategyExpand allstring
sub_updated_atExpand all(string | null)
sub_last_user_agentExpand all(string | null)
online_atExpand all(string | null)
on_hold_expire_durationExpand all(integer | null)
on_hold_timeoutExpand all(string | null)
next_planExpand all(object | null)
usernamestring
statusExpand allstring
used_trafficinteger
lifetime_used_trafficExpand allinteger
created_atstringdate-time
linksExpand allarray<string>
subscription_urlExpand allstring
SystemStatsCollapse allobject
versionstring
mem_totalinteger
mem_usedinteger
cpu_coresinteger
cpu_usagenumber
total_userinteger
online_usersinteger
users_activeinteger
users_on_holdinteger
users_disabledinteger
users_expiredinteger
users_limitedinteger
incoming_bandwidthinteger
outgoing_bandwidthinteger
incoming_bandwidth_speedinteger
outgoing_bandwidth_speedinteger
TokenCollapse allobject
access_tokenstring
token_typeExpand allstring
UnauthorizedCollapse allobject
detailExpand allstring
UserCreateCollapse allobject
proxiesExpand allobject
expireExpand all(integer | null)
data_limitExpand all(integer | null)
data_limit_reset_strategyExpand allstring
inboundsExpand allobject
noteExpand all(string | null)
sub_updated_atExpand all(string | null)
sub_last_user_agentExpand all(string | null)
online_atExpand all(string | null)
on_hold_expire_durationExpand all(integer | null)
on_hold_timeoutExpand all(string | null)
auto_delete_in_daysExpand all(integer | null)
next_planExpand all(object | null)
usernamestring
statusExpand allstring
ExampleExpand allobject
UserDataLimitResetStrategyCollapse allstring
EnumExpand allarray
UserModifyCollapse allobject
proxiesExpand allobject
expireExpand all(integer | null)
data_limitExpand all(integer | null)
data_limit_reset_strategyExpand allstring
inboundsExpand allobject
noteExpand all(string | null)
sub_updated_atExpand all(string | null)
sub_last_user_agentExpand all(string | null)
online_atExpand all(string | null)
on_hold_expire_durationExpand all(integer | null)
on_hold_timeoutExpand all(string | null)
auto_delete_in_daysExpand all(integer | null)
next_planExpand all(object | null)
statusExpand allstring
ExampleExpand allobject
UserResponseCollapse allobject
proxiesobject
expireExpand all(integer | null)
data_limitExpand all(integer | null)
data_limit_reset_strategyExpand allstring
inboundsExpand allobject
noteExpand all(string | null)
sub_updated_atExpand all(string | null)
sub_last_user_agentExpand all(string | null)
online_atExpand all(string | null)
on_hold_expire_durationExpand all(integer | null)
on_hold_timeoutExpand all(string | null)
auto_delete_in_daysExpand all(integer | null)
next_planExpand all(object | null)
usernamestring
statusExpand allstring
used_trafficinteger
lifetime_used_trafficExpand allinteger
created_atstringdate-time
linksExpand allarray<string>
subscription_urlExpand allstring
excluded_inboundsExpand allobject
adminExpand all(object | null)
UserStatusCollapse allstring
EnumExpand allarray
UserStatusCreateCollapse allstring
EnumExpand allarray
UserStatusModifyCollapse allstring
EnumExpand allarray
UserTemplateCreateCollapse allobject
nameExpand all(string | null)
data_limitExpand all(integer | null)
expire_durationExpand all(integer | null)
username_prefixExpand all(string | null)
username_suffixExpand all(string | null)
inboundsExpand allobject
ExampleExpand allobject
UserTemplateModifyCollapse allobject
nameExpand all(string | null)
data_limitExpand all(integer | null)
expire_durationExpand all(integer | null)
username_prefixExpand all(string | null)
username_suffixExpand all(string | null)
inboundsExpand allobject
ExampleExpand allobject
UserTemplateResponseCollapse allobject
nameExpand all(string | null)
data_limitExpand all(integer | null)
expire_durationExpand all(integer | null)
username_prefixExpand all(string | null)
username_suffixExpand all(string | null)
inboundsExpand allobject
idinteger
UserUsageResponseCollapse allobject
node_idExpand all(integer | null)
node_namestring
used_trafficinteger
UserUsagesResponseCollapse allobject
usernamestring
usagesExpand allarray<object>
UsersResponseCollapse allobject
usersExpand allarray<object>
totalinteger
UsersUsagesResponseCollapse allobject
usagesExpand allarray<object>
ValidationErrorCollapse allobject
locExpand allarray<(string | integer)>
msgstring
typestring
