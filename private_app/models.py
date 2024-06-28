from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from core.db import Base


class Meme(Base):
    name: Mapped[str] = mapped_column(unique=True)
    url: Mapped[str | None]
    file_name: Mapped[str | None]
    added: Mapped[datetime] = mapped_column(default=datetime.now)
