from typing import Type

from celery import Celery
from celery.canvas import Signature
from sqlalchemy import event
from sqlalchemy.orm import Session

from cafe.types import OrderId
from .app import celery
from .tasks import BaseTask, CookBurgerTask


TaskType = Type[BaseTask]


class TaskSender:
    app: Celery = celery

    def __init__(self, session: Session) -> None:
        self.session = session

    def send_after_commit(self, task_type: TaskType, kwargs: dict | None = None) -> None:
        @event.listens_for(self.session, 'after_commit')
        def receive_after_commit(_) -> None:
            signature = self.make_signature(task_type.name, kwargs)
            signature.apply_async()

    def make_signature(self, task_name: str, kwargs: dict | None = None) -> Signature:
        return Signature(task_name, kwargs=kwargs, app=self.app)


class TaskScheduler:
    def __init__(self, sender: TaskSender) -> None:
        self.sender = sender


class KitchenScheduler(TaskScheduler):
    def schedule_cook_burger(self, order_id: OrderId) -> None:
        self.sender.send_after_commit(CookBurgerTask, {'order_id': order_id})
