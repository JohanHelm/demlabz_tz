import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    nickname: str
    pass_hash: str
    email: str
    telegram_name: str


class UserPersonalData(BaseModel):
    nickname: str
    email: str
    telegram_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

class UserDataUpdate(UserCreate):
    id: int
    updated_at: datetime.datetime
