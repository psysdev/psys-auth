import jwt

from fastapi import Depends , HTTPException
from fastapi.security import HTTPBearer , HTTPAuthorizationCredentials
#OAuth2PasswordBearer

from app.service.security import verify_access_token

from typing import Annotated

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

bearer_scheme = HTTPBearer()


def get_current_user_id(
    credentials: Annotated[HTTPAuthorizationCredentials,
    Depends(bearer_scheme)]) -> str:
    token = credentials.credentials
    try:
        payload = verify_access_token(token)
        user_id = payload.get(
            "sub"
            )
        
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        return user_id
    
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate":"Bearer"}
        ) 