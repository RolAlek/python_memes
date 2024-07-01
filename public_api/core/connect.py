import os

from fastapi import HTTPException
from httpx import AsyncClient, HTTPStatusError

from core.config import settings


class HTTPManager:
    def __init__(self, url) -> None:
        self.url = url

    async def make_request(
        self,
        method: str,
        endpoint: int | None = None,
        files: dict | None = None,
        data: dict | None = None,
    ):
        try:
            async with AsyncClient() as client:
                response = await client.request(
                    method=method,
                    url=(
                        self.url if not endpoint
                        else os.path.join(self.url, str(endpoint))
                    ),
                    files=files,
                    data=data,
                )
                response.raise_for_status()
        except HTTPStatusError as error:
            raise HTTPException(
            status_code=error.response.status_code,
            detail=error.response.json().get('detail')
        ) from error
        return response.json()


http_manager = HTTPManager(url=settings.service_url)
