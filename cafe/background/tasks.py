import time

from celery import Task

from .app import celery


class BaseTask(Task):
    app = celery
    name: str
    abstract = True

    def run(self, *args, **kwargs) -> None:
        raise NotImplementedError()


class PrepareOrderTask(BaseTask):
    name = 'cook_burger'

    def run(self, order_id) -> None:
        time.sleep(10)


celery.register_task(PrepareOrderTask)
