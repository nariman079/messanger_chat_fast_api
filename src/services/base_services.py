import hashlib
from datetime import timedelta, datetime

import jwt

from config.settings import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM
from src.models.base_models import User


async def hash_password(password, salt):
    password_hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    return password_hash

async def verify_password(stored_password, provided_password, salt = SECRET_KEY):
    password_hash = hashlib.sha256((provided_password + salt).encode('utf-8')).hexdigest()
    print(provided_password, stored_password, password_hash, password_hash == stored_password)
    return password_hash == stored_password

async def set_user_hashed_password(password: str, user: User) -> User:
    user.hashed_password = await hash_password(password, SECRET_KEY)
    return user

async def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Создание JWT-токена."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
