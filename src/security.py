from math import frexp
from typing import Annotated

from fastapi import status, Depends, HTTPException, Path
import jwt
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from sqlalchemy.ext.asyncio import AsyncSession

from config.settings import SECRET_KEY, ALGORITHM
from migrations.versions.ce5eb6c82eb9_ import depends_on
from src.database import get_db
from src.models.base_models import User, Friend
from src.services.db_services import get_user, get_user_by_id

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(
        token: Annotated[oauth2_scheme, Depends()],
        db: Annotated[get_db, Depends()]
) -> User:
    """Проверка токена и возвращение пользователя."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except PyJWTError:
        raise credentials_exception

    user = await get_user(db, email)
    if user is None:
        raise credentials_exception
    return user

async def get_fiend(
        friend_id: Annotated[int, Path()],
        db: Annotated[get_db, Depends()]
) -> User:
    friend = await get_user_by_id(
        db, friend_id
    )
    if friend is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Такого пользователя не существует"
        )
    return friend

async def is_not_added_friend() -> bool:
    return True

async def check_opportunity_add_friend(
    friend: Annotated[get_fiend, Depends()],
    user: Annotated[get_current_user, Depends()]
) -> User:
    if is_not_added_friend():
        raise HTTPException(
            detail="Нельзя добавлять самого себя",
            status_code=status.HTTP_409_CONFLICT
        )
    return friend