from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from cafe.config import Settings


def get_engine(settings: Settings) -> Engine:
    return create_engine(settings.sqlalchemy_url, connect_args={'check_same_thread': False}, echo=True)


class SessionFactory:
    def __init__(self, settings: Settings) -> None:
        self.engine = get_engine(settings)
        self.factory = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def __call__(self) -> Session:
        return self.factory()
