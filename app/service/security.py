from pwdlib import PasswordHash

from datetime import datetime, timedelta, timezone
from pathlib import Path

import jwt

from app.core.config import settings

public_key_path = Path(
    "keys/public.pem"
)

password_hash = PasswordHash.recommended()

def hash_password(password:str) -> str:
    return password_hash.hash(password)

def verify_password(password:str,hashed:str)->bool:
    return password_hash.verify(password,hashed)

def verify_access_token(token: str ) -> dict:
    public_key = public_key_path.read_text(
        encoding="utf-8"
        )

    return jwt.decode(
        token,
        public_key,
        algorithms=["RS256"],
        issuer=settings.jwt_issuer,
        options={"require": ["sub","iss","iat","exp"]}
    )