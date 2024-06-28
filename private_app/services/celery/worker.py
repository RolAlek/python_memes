from celery import Celery

from core.config import settings

app = Celery(
    __name__,
    broker=settings.celery.broker,
    backend=settings.celery.backend
)
