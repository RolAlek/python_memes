from fastapi import FastAPI

from public_app.api import router
from public_app.core.config import settings


app = FastAPI(title=settings.app_title)
app.include_router(router, prefix='/memes', tags=['Memes'])
