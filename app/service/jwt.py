from datetime import datetime, timezone, timedelta
from pathlib import Path

import jwt

from app.core.config import settings

def create_access_token(user_id:str) -> str:
    private_key = Path(
        settings.private_key_path
        ).read_text(
            encoding="utf-8"
        )

    now = datetime.now(timezone.utc)

    payload = {
        "sub": user_id,
        "iss": settings.jwt_issuer,
        "iat": now,
        "exp": now + timedelta(
            minutes=settings.jwt_access_token_minutes
        )
    }

    return jwt.encode(
        payload,
        private_key,
        algorithm="RS256"
    )