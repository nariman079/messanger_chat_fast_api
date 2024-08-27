from typing import Sequence

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from src.schemas.auth_schemas import UserRegister, UserLogin, UserToken, UserBase
from src.models.base_models import User
from src.services.base_services import set_user_hashed_password, verify_password, create_access_token
from src.services.db_services import get_user


async def get_user_list_service(
        db: AsyncSession
) -> Sequence[User]:
    """Логика получения списка пользователей"""
    query = await db.execute(
        select(
            User
        )
    )
    user_list = query.scalars().all()
    return user_list

async def user_login_service(
        user: UserLogin,
        db: AsyncSession
) -> UserToken:
    """Логика авторизации  пользователей"""
    db_user = await get_user(db, user.email)

    if not user:
        raise HTTPException(
            detail="This user not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

    is_verify = await verify_password(
        db_user.hashed_password, user.password
    )


    if is_verify:
        token = await create_access_token({"sub": db_user.email})
        return UserToken(
            email=user.email,
            token=token
        )
    else:
        raise HTTPException(
            detail="Authenticate error",
            status_code=status.HTTP_400_BAD_REQUEST
        )

async def user_register_service(
        user: UserRegister,
        db: AsyncSession
) -> UserBase:
    """ Логика регистрации пользователя """
    db_user = User(**user.dict())
    new_user = await set_user_hashed_password(
        user.hashed_password,
        db_user
    )
    db.add(new_user)
    await db.commit()
    return user
