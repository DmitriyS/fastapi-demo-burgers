from __future__ import annotations

from contextlib import ContextDecorator
from typing import Type

from billiard.einfo import Traceback
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from cafe.config import Settings, get_settings


def get_engine(settings: Settings) -> Engine:
    return create_engine(settings.sqlalchemy_url, connect_args={'check_same_thread': False}, echo=True)


class SessionFactory:
    def __init__(self, settings: Settings) -> None:
        self.engine = get_engine(settings)
        self.factory = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def __call__(self) -> Session:
        return self.factory()


def get_session_factory() -> SessionFactory:
    return SessionFactory(get_settings())


class SimpleTransaction(ContextDecorator):
    def __init__(self, session: Session) -> None:
        self.session = session

    def __enter__(self) -> SimpleTransaction:
        return self

    def __exit__(self, exc_type: Type[Exception] | None, exc_val: Exception | None, exc_tb: Traceback | None) -> None:
        if exc_type is None:
            self.session.commit()
        else:
            if self.session.is_active:
                self.session.rollback()

        self.session.close()


def transaction(session: Session) -> SimpleTransaction:
    return SimpleTransaction(session)
