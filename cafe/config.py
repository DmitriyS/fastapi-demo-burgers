from pydantic import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_url: str = 'sqlite://'

    celery_broker_url: str = 'file://'
    celery_result_backend: str = 'file://'
    celery_imports: tuple[str, ...] = ('cafe.background.tasks',)
    celery_always_eager: bool = False

    class Config:
        env_file = '.env'


settings: Settings = Settings()
