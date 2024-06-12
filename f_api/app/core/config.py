from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    SALT: str

    def async_database_url(self):
        return f"postgresql+asyncpg://" \
               f"{self.POSTGRES_USER}:" \
               f"{self.POSTGRES_PASSWORD}@" \
               f"{self.POSTGRES_HOST}:" \
               f"{self.POSTGRES_PORT}/" \
               f"{self.POSTGRES_DB}"

    def jwt_settigs_dict(self):
        return {"secret_key": self.SECRET_KEY,
                "algoritm": self.ALGORITHM,
                "expire": self.ACCESS_TOKEN_EXPIRE_MINUTES,
                "salt": self.SALT
                }

    class Config:
        env_file = ".env"


settings = Settings()
