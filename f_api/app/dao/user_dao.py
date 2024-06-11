from abc import ABC, abstractmethod
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import User
from app.db.db_settings import get_async_session


class UserDAO(ABC):

    @abstractmethod
    async def get_user(self, username: str) -> User:
        pass


class SqlAlchemyUserDAO(UserDAO):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user(self, username: str) -> User:
        result = await self.session.execute(select(User).where(User.nickname == username))
        return result.scalars().first()


async def get_user_dao(session: AsyncSession = Depends(get_async_session)) -> SqlAlchemyUserDAO:
    return SqlAlchemyUserDAO(session)
