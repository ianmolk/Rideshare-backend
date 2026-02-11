from datetime import datetime, timedelta, timezone
from typing import Any, Dict 

import jwt
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

from app.core.config import settings

ph = PasswordHasher()

def hash_password(password: str) -> str:
    return ph.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    try:
        return ph.verify(hashed, password)
    except VerifyMismatchError:
        return False
    except Exception:
        return False
    

def create_access_token(subject: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload: Dict[str, Any] = {
        "sub": subject,
        "exp": expire
    }

    token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALG)

    if isinstance(token, bytes):
        token = token.decode("utf-8")

    return token