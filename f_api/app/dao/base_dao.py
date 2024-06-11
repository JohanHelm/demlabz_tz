from abc import ABC, abstractmethod

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractDAO(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, username: str):
        raise NotImplementedError


class DAO(AbstractDAO):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict):
        query = insert(self.model).values(**data).returning(self.model)
        await self.session.execute(query)
        await self.session.commit()

    async def get_one(self, username: str):
        query = select(self.model).where(self.model.nickname == username)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def update_one(self, new_data: dict):
        await self.session.commit()
        await self.session.refresh(new_data)
