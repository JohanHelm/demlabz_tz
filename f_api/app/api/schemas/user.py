import datetime

from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    nickname: str
    pass_hash: str
    email: str
    telegram_name: str


class UserPersonalData(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nickname: str
    email: str
    telegram_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

class UserDataUpdate(UserCreate):
    id: int
    updated_at: datetime.datetime
