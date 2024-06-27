from celery import Celery

from private_app.core.config import settings

app = Celery(
    __name__,
    broker=settings.celery.broker,
    backend=settings.celery.backend
)
