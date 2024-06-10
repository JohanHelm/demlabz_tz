from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from sqlalchemy.future import select

from app.db import models


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def get_user(username: str, db_session: AsyncSession):
    result = await db_session.execute(select(models.User).where(models.User.nickname == username))
    return result.scalars().first()


async def authenticate_user(db_session: AsyncSession, username: str, password: str):
    user = await get_user(username, db_session)
    if not user or not verify_password(password, user.pass_hash):
        return False
    return True
