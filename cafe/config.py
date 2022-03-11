from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_url: str = 'sqlite://'

    celery_broker_url: str = 'file://'
    celery_result_backend: str = 'file://'
    celery_always_eager: bool = False

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings() -> Settings:
    return Settings()
