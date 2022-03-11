from celery import Celery

from cafe import background
from cafe.config import Settings, get_settings


settings: Settings = get_settings()

celery: Celery = Celery(
    settings.project_name,
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend,
    task_always_eager=settings.celery_task_always_eager,
)

celery.autodiscover_tasks(packages=(background.__name__,))
