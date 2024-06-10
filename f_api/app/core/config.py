from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # @property
    def async_database_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # @property
    def jwt_settigs_dict(self):
        return {"secret_key": self.SECRET_KEY, "algoritm": self.ALGORITHM, "expire": self.ACCESS_TOKEN_EXPIRE_MINUTES}

    class Config:
        env_file = ".env"


settings = Settings()
