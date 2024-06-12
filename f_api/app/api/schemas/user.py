import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    nickname: str
    open_pass: str
    email: str = ""
    telegram_name: str = ""


class UserPersonalData(UserBase):
    nickname: str
    email: str
    telegram_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UserUpdate(UserBase):
    open_pass: Optional[str] = None
    email: Optional[str] = None
    telegram_name: Optional[str] = None
