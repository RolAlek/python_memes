import asyncio
from http import HTTPStatus
from typing import Any
import uuid

from celery.result import AsyncResult, states
from fastapi import HTTPException, UploadFile

from app.core.config import settings
from app.services.celery.tasks import delete_in_s3, upload_to_s3



async def wait_task(task: AsyncResult, delay: float | int = 0.5):
    while task.state not in (states.SUCCESS, states.FAILURE):
        await asyncio.sleep(delay)
    if task.state != states.SUCCESS:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail='Во время загрузки мема произошел мем!',
        )
    return task.result


async def file_upload(file: UploadFile)-> tuple[str, Any]:
    content_type = file.content_type
    if content_type not in ('image/jpeg', 'image/png'):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Этот мем не смешной!'
        )
    filename = f'{str(uuid.uuid4())}.{file.filename.split(".")[-1]}'
    task = upload_to_s3.delay(
        settings.minio.bucket,
        filename,
        await file.read(),
        content_type
    )
    return filename, await wait_task(AsyncResult(task.id))


async def file_delete(filename: str):
    delete_in_s3.delay(settings.minio.bucket, filename)
