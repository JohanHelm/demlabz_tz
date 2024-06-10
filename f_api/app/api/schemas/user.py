import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    nickname: str
    pass_hash: str
    email: str
    telegram_name: str


class UserGetFromDB(UserCreate):
    id: int
    created_at: datetime.datetime


class UserDataUpdate(UserCreate):
    updated_at: datetime.datetime
