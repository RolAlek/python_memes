from http import HTTPStatus

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from schemas import ResponseMeme
from core import http_manager


router = APIRouter()


@router.post('/', response_model=ResponseMeme)
async def add_meme(
    name: str = Form(...),
    file: UploadFile = File(...),
):
    if name is None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='То что уже мертво - умереть не может!'
        )
    if file.content_type not in ('image/jpeg', 'image/png'):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Этот мемасик не смешной или вообще не мемасик!',
        )
    return await http_manager.make_request(
        method='POST',
        files={'file': (file.filename, file.file, file.content_type)},
        data={'name': name},
    )


@router.get('/', response_model=list[ResponseMeme])
async def get_memes():
    return await http_manager.make_request(method='GET')


@router.get('/{id}', response_model=ResponseMeme)
async def get_meme(id: int):
    return await http_manager.make_request(method='GET', endpoint=id)


@router.put('/{id}', response_model=ResponseMeme)
async def change_meme(
    id: int,
    name: str | None = Form(None),
    file: UploadFile | None = File(None),
):
    if name is None and file is None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Одно из полей должно быть заполнено.',
        )
    return await http_manager.make_request(
        method='PUT',
        endpoint=id,
        files=(
            {'file': (file.filename, file.file, file.content_type)}
            if file else None
        ),
        data={'name': name} if name else None,
    )


@router.delete('/{id}')
async def delete_meme(id: int):
    return await http_manager.make_request(method='DELETE', endpoint=id)
