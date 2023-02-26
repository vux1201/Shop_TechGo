from typing import Any
from datetime import datetime, timedelta
import jwt

from core.config import settings


def create_access_token(subject: str | Any):
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, key=settings.SECRET_KEY)
    return encoded_jwt
