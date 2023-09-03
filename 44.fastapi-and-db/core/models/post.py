from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user import User


class Post(Base):
    title: Mapped[str] = mapped_column(String(100))
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )

    author_id: Mapped[int] = mapped_column(
        # ForeignKey(User.id)
        ForeignKey("users.id")
    )
    author: Mapped["User"] = relationship(back_populates="posts")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id},"
            f" title={self.title!r},"
            f" author_id={self.author_id})"
        )

    def __repr__(self):
        return str(self)
