from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from datetime import datetime, timedelta
import os
from typing import Dict, Any, Optional

from ...utils.logging import get_logger

logger = get_logger('jwt_auth')

security = HTTPBearer(auto_error=False)

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev-secret-key-change-in-production")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXPIRATION_HOURS = int(os.getenv("JWT_EXPIRATION_HOURS", "24"))

def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=JWT_EXPIRATION_HOURS)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM], audience="ideamark-api")
        return payload
    except JWTError as e:
        logger.warning(f"JWT verification failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

async def get_current_user(credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)) -> Dict[str, Any]:
    if not credentials:
        return {
            "sub": "anonymous",
            "admin": False,
            "authenticated": False
        }
    
    try:
        payload = verify_token(credentials.credentials)
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        return {
            "sub": user_id,
            "iss": payload.get("iss"),
            "aud": payload.get("aud"),
            "admin": payload.get("admin", False),
            "authenticated": True,
            "exp": payload.get("exp"),
            "scopes": payload.get("scopes", []),
            "permissions": payload.get("permissions", {})
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error validating token: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

def create_dev_token(user_id: str = "dev-user", admin: bool = True) -> str:
    data = {
        "sub": user_id,
        "iss": "ideamark-mcp-server",
        "aud": "ideamark-api",
        "admin": admin,
        "iat": datetime.utcnow(),
        "scopes": ["read", "write"],
        "permissions": {
            "patterns": ["read", "write"],
            "refs": ["generate"],
            "merge": ["execute"]
        }
    }
    return create_access_token(data)
