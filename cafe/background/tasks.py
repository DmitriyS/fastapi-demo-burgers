import time
from typing import Any

from celery import Task

from .app import celery
from ..types import OrderId


class BaseTask(Task):
    app = celery
    name: str
    abstract: bool = True

    def run(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError()


class CookBurgerTask(BaseTask):
    name: str = 'cook_burger'

    def run(self, order_id: OrderId) -> None:
        time.sleep(10)


celery.register_task(CookBurgerTask)
