from pydantic import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_url: str = 'sqlite://'

    class Config:
        env_file = '.env'


settings: Settings = Settings()
