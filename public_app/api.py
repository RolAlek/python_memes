from http import HTTPStatus

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from httpx import AsyncClient, HTTPStatusError

from core.shcemas import ResponseMeme
from public_app.core import http_manager
from public_app.core.config import settings


router = APIRouter()


@router.post('/', response_model=ResponseMeme)
async def add_meme(
    name: str = Form(...),
    file: UploadFile = File(...),
):
    try:
        async with AsyncClient() as client:
            response = await client.post(
                url=settings.service_url,
                files={'file': (file.filename, file.file, file.content_type)},
                data={'name': name},
            )
    except HTTPStatusError as error:
        raise HTTPException(
            status_code=error.response.status_code,
            detail=str(error)
        ) from error
    return response.json()


@router.get('/', response_model=list[ResponseMeme])
async def get_memes():
    response = await http_manager.get_method()
    return response.json()


@router.get('/{id}', response_model=ResponseMeme)
async def get_meme(id: int):
    response = await http_manager.get_method(id)
    return response.json()


@router.put('/{id}', response_model=ResponseMeme)
async def change_meme(
    id: int,
    name: str | None = Form(None),
    file: UploadFile | None = File(None),
):
    if name is None and file is None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Одо из полей должно быть заполнено.',
        )
    try:
        async with AsyncClient() as client:
            response = await client.put(
                url=f'{settings.service_url}{id}',
                files=(
                    {'file': (file.filename, file.file, file.content_type)}
                    if file else None
                ),
                data={'name': name} if name else None,
            )
    except HTTPStatusError as error:
        raise HTTPException(
            status_code=error.response.status_code,
            detail=str(error)
        ) from error
    return response.json()


@router.delete('/{id}')
async def delete_meme(id: int):
    try:
        async with AsyncClient() as client:
            response = await client.delete(url=f'{settings.service_url}{id}')
    except HTTPStatusError as error:
        raise HTTPException(
            status_code=error.response.status_code,
            detail=str(error)
        ) from error
    return response.json()
