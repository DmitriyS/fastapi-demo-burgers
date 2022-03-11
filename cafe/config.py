from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    project_name: str = 'Cafe'

    sqlalchemy_url: str = 'sqlite://'

    celery_broker_url: str = 'redis://'
    celery_result_backend: str = 'redis://'
    celery_always_eager: bool = False

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings() -> Settings:
    return Settings()
