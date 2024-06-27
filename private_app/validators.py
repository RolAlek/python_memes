from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from private_app.crud import get_by_name, get_single
from private_app.models import Meme


async def check_exist_meme_by_name(name: str, session: AsyncSession) -> str:
    if await get_by_name(name, session):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Don't repeat yourself!",
        )
    return name


async def get_meme_or_404(id: int, session: AsyncSession) -> Meme:
    meme = await get_single(id, session)
    if meme is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Такого мема в нашей мематеке пока нет!'
        )
    return meme
