from fastapi import FastAPI

from api import router
from core.config import settings


app = FastAPI(title=settings.app_title)
app.include_router(router, prefix='/memes', tags=['Memes'])
