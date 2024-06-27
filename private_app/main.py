from fastapi import FastAPI

from private_app.api import router
from private_app.core.config import settings

app = FastAPI(title=settings.app_title)
app.include_router(router, prefix='/services', tags=['Services'])
