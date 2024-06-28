from typing import Sequence

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Meme
from schemas import CreateMeme, UpdateMeme


async def create_meme(meme: CreateMeme, session: AsyncSession) -> Meme:
    db_obj = Meme(**meme.model_dump())
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj


async def get_multi(session: AsyncSession) -> Sequence[Meme]:
    memes = await session.scalars(select(Meme))
    return memes.all()


async def get_single(id: int, session: AsyncSession) -> Meme | None:
    meme = await session.get(Meme, id)
    return meme


async def get_by_name(name: str, session: AsyncSession) -> Meme | None:
    meme = await session.scalars(
        select(Meme).where(Meme.name == name)
    )
    return meme.first()

async def meme_update(
    meme: Meme,
    data: UpdateMeme,
    session: AsyncSession,
) -> Meme:
    new_data = data.model_dump(exclude_unset=True)
    meme_data = jsonable_encoder(meme)
    for field in meme_data:
        if field in new_data:
            setattr(meme, field, new_data[field])

    session.add(meme)
    await session.commit()
    await session.refresh(meme)
    return meme


async def meme_delete(meme: Meme, session: AsyncSession) -> Meme:
    await session.delete(meme)
    await session.commit()
    return meme
