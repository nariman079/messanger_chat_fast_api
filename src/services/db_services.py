from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_object
from src.models.base_models import User


async def get_user(db: AsyncSession, email: str):
    return await get_object(
        db=db,
        obj=User,
        by_field='email',
        search_value=email
    )

async def get_user_by_id(db: AsyncSession, id: int):
    return await get_object(
        db=db,
        obj=User,
        by_field='id',
        search_value=id
    )

