from abc import ABC, abstractmethod

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.user import UserCreate
from app.db.models import User


class UserDAO(ABC):  # это абстрактный интерфейс нашего репозитория

    @abstractmethod
    async def create_todo(self, user: UserCreate) -> User:
        pass


class SqlAlchemyUserDAO(UserDAO):
    def __init__(self, session: AsyncSession):
        self.session = session

    # далее, по сути, код из эндпоинтов с предыдущего шага
    async def get_todos(self) -> list[ToDo]:
        result = await self.session.execute(select(ToDo))
        return result.scalars().all()

    async def create_todo(self, todo: ToDoCreate) -> ToDo:
        new_todo = ToDo(**todo.model_dump())
        self.session.add(new_todo)
        await self.session.commit()
        await self.session.refresh(new_todo)
        return new_todo