from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .post import Post


class User(Base):
    username: Mapped[str] = mapped_column(String(30), unique=True)
    email: Mapped[str]
    motto: Mapped[str | None]

    posts: Mapped[list["Post"]] = relationship(back_populates="author")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id},"
            f" username={self.username!r},"
            f" email={self.email!r},"
            f" motto={self.motto!r})"
        )

    def __repr__(self):
        return str(self)
