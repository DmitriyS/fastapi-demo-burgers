import random
import time
from datetime import datetime
from typing import Any

from celery import Celery, Task

from cafe.database import get_session_factory
from cafe.service import Cafe, create_service
from cafe.types import OrderId
from .app import celery


class BaseTask(Task):
    app: Celery = celery
    name: str
    abstract: bool = True

    def run(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError()


class SimpleTransactionalTask(BaseTask):
    session_factory = get_session_factory()

    def __init__(self) -> None:
        self.session = self.session_factory()

    def run(self, *args: Any, **kwargs: Any) -> None:
        try:
            self.run_in_transaction(*args, **kwargs)
            self.session.commit()
        except Exception:
            if self.session.is_active:
                self.session.rollback()
            raise
        finally:
            self.session.close()

    def run_in_transaction(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError()


class CookBurgerTask(SimpleTransactionalTask):
    name: str = 'cook_burger'

    def run_in_transaction(self, order_id: OrderId) -> None:
        wait_random_time()
        self.service.prepare_order(order_id, datetime.now())

    @property
    def service(self) -> Cafe:
        return create_service(self.session)


def wait_random_time(low: int = 1, high: int = 10) -> None:
    time.sleep(random.randint(low, high))


celery.register_task(CookBurgerTask)
