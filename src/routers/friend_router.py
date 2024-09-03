from typing import Any, Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.models.base_models import User
from src.security import get_current_user, check_opportunity_add_friend

friend_router = APIRouter(
    prefix='/auth'
)


@friend_router.get('/me/friends/')
async def get_my_friends():
    """Список моих друзей"""
    ...

@friend_router.post(
    '/me/friends/{friend_id}/add-or-delete-friend/',
    name="add_friend"
)
async def add_friend(
    friend: Annotated[
        check_opportunity_add_friend,
        Depends()
    ]
):
    """Добавление друга"""
    return {
        'test'
    }


@friend_router.delete('/me/friends/{friend_id}/add-or-delete-friend/')
async def delete_friend():
    """Удаление друга"""
    ...
