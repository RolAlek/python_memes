from datetime import datetime

from pydantic import BaseModel


class ResponseMeme(BaseModel):
    id: int
    name: str
    url: str
    added: datetime

    class Config:
        orm_mod = True
