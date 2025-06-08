from fastapi import Depends, Request
from fastapi.security import HTTPAuthorizationCredentials
from typing import Optional, Dict, Any
import os

AUTH_DISABLED = os.getenv("AUTH_DISABLED", "false").lower() in ["1", "true", "yes"]

from .jwt_auth import get_current_user as get_jwt_user, security
from .oauth import get_current_oauth_user


async def get_current_user(
    request: Request,
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
) -> Dict[str, Any]:
    """Resolve the current user via OAuth cookie, JWT header, or return an
    anonymous admin user if authentication is disabled."""

    if AUTH_DISABLED:
        return {"sub": "anonymous", "admin": True, "authenticated": False}

    oauth_user = await get_current_oauth_user(request)
    if oauth_user.get("authenticated"):
        return oauth_user
    return await get_jwt_user(credentials)
