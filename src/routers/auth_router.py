from typing import Any, Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.models.base_models import User
from src.schemas.auth_schemas import UserLogin, UserRegister, UserBase, UserToken
from src.security import get_current_user
from src.services.auth_services import get_user_list_service, user_register_service, user_login_service

auth_router = APIRouter(
    prefix='/auth'
)

@auth_router.post('/login/', name='user_login')
async def user_login(
    user: UserLogin,
    db: Annotated[
        AsyncSession,
        Depends(get_db)
    ] = ...
) -> UserToken:
    """Авторизация и получение токена"""
    return await user_login_service(user, db)

@auth_router.post('/register/', name='user_register')
async def user_register(
    user: UserRegister,
    db: Annotated[
        AsyncSession,
        Depends(get_db)
    ]
) -> UserBase:
    """Регистрация пользователя"""
    return await user_register_service(
        user,
        db
    )

@auth_router.get('/users/', response_model=list[UserRegister], name='user_list')
async def get_user_list(
        db: Annotated[
            AsyncSession,
            Depends(get_db)
        ] = ...,
        auth_user: Annotated[
            User,
            Depends(get_current_user)
        ] = ...
) -> Any:
    return await get_user_list_service(db)