"""Password and JWT helpers used by the student controller implementations."""
from datetime import datetime, timedelta, timezone
from jose import jwt
from pwdlib import PasswordHash
from app.core.config import settings


_pwd = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return _pwd.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return _pwd.verify(password, hashed_password)

def create_access_token(subject: str, role: str) -> str:
    expires = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    return jwt.encode({"sub": subject, "role": role, "exp": expires}, settings.secret_key, algorithm=settings.algorithm)

def decode_access_token(token: str) -> dict:
    return jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
