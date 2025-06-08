from fastapi import APIRouter, Request, HTTPException, Depends, status
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.security import OAuth2AuthorizationCodeBearer
from authlib.integrations.starlette_client import OAuth, OAuthError
import os
from typing import Dict, Any, Optional

from .jwt_auth import create_access_token, verify_token, security

router = APIRouter()

OAUTH_CLIENT_ID = os.getenv("OAUTH_CLIENT_ID")
OAUTH_CLIENT_SECRET = os.getenv("OAUTH_CLIENT_SECRET")
OAUTH_AUTH_URL = os.getenv("OAUTH_AUTHORIZATION_URL")
OAUTH_TOKEN_URL = os.getenv("OAUTH_TOKEN_URL")
OAUTH_REDIRECT_URI = os.getenv("OAUTH_REDIRECT_URI")
OAUTH_SCOPE = os.getenv("OAUTH_SCOPE", "openid profile email")


# OAuth client using Authlib
_oauth = OAuth()
_oauth.register(
    name="default",
    client_id=OAUTH_CLIENT_ID,
    client_secret=OAUTH_CLIENT_SECRET,
    access_token_url=OAUTH_TOKEN_URL,
    authorize_url=OAUTH_AUTH_URL,
    client_kwargs={"scope": OAUTH_SCOPE},
)


def get_oauth_client():
    """Return configured OAuth client."""
    return _oauth.create_client("default")


@router.get("/oauth/login")
async def login_redirect(request: Request):
    """Redirect user to external authorization server."""
    client = get_oauth_client()
    redirect_uri = OAUTH_REDIRECT_URI
    return await client.authorize_redirect(request, redirect_uri)


@router.get("/oauth/callback")
async def oauth_callback(request: Request):
    """Handle OAuth provider callback and issue JWT."""
    client = get_oauth_client()
    try:
        token = await client.authorize_access_token(request)
        user = await client.parse_id_token(request, token)
    except OAuthError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    jwt_token = create_access_token({"sub": user.get("sub")})
    response = JSONResponse({"access_token": jwt_token, "token_type": "bearer"})
    response.set_cookie("access_token", jwt_token, httponly=True)
    return response


oauth_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="/oauth/login",
    tokenUrl="/oauth/callback",
    auto_error=False,
)


async def get_current_oauth_user(
    request: Request,
    token: Optional[str] = Depends(oauth_scheme),
) -> Dict[str, Any]:
    """Retrieve current user from OAuth cookie or Authorization header."""
    if not token:
        token = request.cookies.get("access_token")
    if not token:
        return {"sub": "anonymous", "admin": False, "authenticated": False}

    try:
        payload = verify_token(token)
        return {
            "sub": payload.get("sub"),
            "admin": payload.get("admin", False),
            "authenticated": True,
            "exp": payload.get("exp"),
        }
    except HTTPException:
        raise
    except Exception:
        return {"sub": "anonymous", "admin": False, "authenticated": False}
