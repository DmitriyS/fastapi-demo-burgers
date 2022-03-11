from celery import Celery

from cafe import background
from cafe.config import Settings, get_settings


settings: Settings = get_settings()

celery: Celery = Celery(
    'Cafe',
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend,
)

celery.autodiscover_tasks(packages=(background.__name__,))
