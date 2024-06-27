import os

from fastapi import HTTPException
from httpx import AsyncClient, HTTPStatusError, Response

from public_app.core.config import settings


class HTTPManager:
    def __init__(self, url) -> None:
        self.url = url

    async def get_method(self, id: int = None) -> Response:
        try:
            async with AsyncClient() as client:
                response = await client.get(
                    url=os.path.join(self.url, str(id)) if id else self.url
                )
        except HTTPStatusError as error:
            raise HTTPException(
                status_code=error.response.status_code,
                detail=str(error)
            ) from error
        return response

http_manager = HTTPManager(url=settings.service_url)
