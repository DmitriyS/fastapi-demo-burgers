from pydantic import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_url: str = 'sqlite://'
    celery_broker_url: str = 'file://'
    celery_result_backend: str = 'file://'
    celery_imports = ('cafe.background.tasks',)

    class Config:
        env_file = '.env'


settings: Settings = Settings()
