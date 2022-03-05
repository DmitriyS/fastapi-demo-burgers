from celery import Celery

from cafe.config import Settings


settings: Settings = Settings()

celery: Celery = Celery('Cafe')
celery.conf.broker_url = settings.celery_broker_url
celery.conf.result_backend = settings.celery_result_backend
celery.conf.imports = settings.celery_imports

celery.autodiscover_tasks()
