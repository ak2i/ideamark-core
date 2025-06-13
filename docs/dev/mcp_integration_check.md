# MCP Authentication Integration Check

This update reviews the slideshow at [https://slide-tubone24.pages.dev/slides/authmcp/1.html](https://slide-tubone24.pages.dev/slides/authmcp/1.html) and compares its recommendations with the current `mcp_server` implementation.

## Key Points from the Slides

- Emphasize that remote MCP servers must implement strong authentication and authorization.
- OAuth 2.1 with **PKCE** is required for public clients.
- Clients should obtain metadata from `.well-known/oauth-authorization-server` (server **SHOULD**, client **MUST**).
- The MCP server must also expose **Protected Resource Metadata** as specified in RFC 9728 (**MUST**).
- Authentication results in **two access tokens**: one between the MCP client and server, and another between the MCP server and external services. A mechanism (e.g., a TTL key-value store) is recommended to associate them.
- Demonstrations show dynamic client registration (DCR) to automatically create OAuth clients.

## Current Repository Implementation

- OAuth logic lives in [`lib/mcp_server/auth/oauth.py`](../../lib/mcp_server/auth/oauth.py). It provides `/oauth/login` and `/oauth/callback` endpoints using Authlib and issues a JWT for API calls.
- **PKCE**, metadata discovery endpoints, and DCR are **not** implemented.
- Only a single JWT token is issued; there is no token passthrough to external services.
- The server supports JWT authentication via [`jwt_auth.py`](../../lib/mcp_server/auth/jwt_auth.py) but lacks advanced OAuth 2.1 features.

## Conclusion

The slides outline a more comprehensive OAuth 2.1 approach than currently implemented. Adding PKCE verification, metadata discovery endpoints, protected resource metadata, and dynamic client registration would align the server with the recommended MCP authentication model.
