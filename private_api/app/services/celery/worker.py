from celery import Celery

from app.core.config import settings

app = Celery(
    __name__,
    broker=settings.celery.broker,
    backend=settings.celery.backend
)
