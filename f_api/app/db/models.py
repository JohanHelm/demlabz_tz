import datetime

from sqlalchemy import BigInteger, DateTime, func, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.db_settings import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    nickname: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    pass_hash: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str]
    telegram_name: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())

