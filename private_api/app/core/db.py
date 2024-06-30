from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declared_attr,
    mapped_column
)
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.core.config import settings


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    @classmethod
    def __tablename__(cls):
        return f'{cls.__name__.lower()}s'

    id: Mapped[int] = mapped_column(primary_key=True)


class DBManager:

    def __init__(self, url: str, echo: bool) -> None:
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
        )

    async def dispose(self):
        await self.engine.dispose()

    async def get_async_session(self):
        async with self.session_factory() as session:
            yield session


db_manager = DBManager(str(settings.db.url), settings.db.echo)
