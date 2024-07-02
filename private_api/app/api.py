from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import ResponseMeme
from app.core import db_manager
from app.core.utils import file_delete, file_upload
from app.crud import create_meme, get_multi, meme_delete, meme_update
from app.schemas import CreateMeme, UpdateMeme
from app.validators import check_exist_meme_by_name, get_meme_or_404

router = APIRouter()


@router.post('/', response_model=ResponseMeme, status_code=201)
async def upload_meme(
    file: UploadFile = File(...),
    name: str = Form(...),
    session: AsyncSession = Depends(db_manager.get_async_session),
):
    await check_exist_meme_by_name(name, session)
    meme = await create_meme(CreateMeme(name=name), session)
    filename, url = await file_upload(file)
    return await meme_update(
        meme=meme,
        data=UpdateMeme(url=url, file_name=filename),
        session=session
    )


@router.get('/', response_model=list[ResponseMeme])
async def get_memes(
    session: AsyncSession = Depends(db_manager.get_async_session),
):
    return await get_multi(session)


@router.get('/{id}', response_model=ResponseMeme)
async def get_meme(
    id: int,
    session: AsyncSession = Depends(db_manager.get_async_session),
):
    return await get_meme_or_404(id, session)


@router.put('/{id}', response_model=ResponseMeme)
async def change_meme(
    id: int,
    name: str | None = Form(None),
    file: UploadFile | None = File(None),
    session: AsyncSession = Depends(db_manager.get_async_session),
):
    meme = await get_meme_or_404(id, session)
    data={}
    if name:
        data['name'] = await check_exist_meme_by_name(name, session)
    if file:
        data['filename'], data['url'] = await file_upload(file)
    data = UpdateMeme(**data)
    return await meme_update(meme, data, session)


@router.delete('/{id}')
async def delete_meme(
    id: int,
    session: AsyncSession = Depends(db_manager.get_async_session),
):
    meme = await get_meme_or_404(id, session)
    filename = meme.file_name
    await file_delete(filename)
    return await meme_delete(
        await get_meme_or_404(id, session),
        session,
    )
