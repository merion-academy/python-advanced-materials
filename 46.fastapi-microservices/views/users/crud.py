from typing import Sequence

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User

from .schemas import UserCreateSchema, UserUpdateSchema


async def create_user(session: AsyncSession, user_create: UserCreateSchema) -> User:
    user = User(**user_create.model_dump())
    async with session.begin():
        session.add(user)
    return user


async def get_users(session: AsyncSession) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result = await session.execute(stmt)
    users = result.scalars().all()
    # users = await session.scalars(stmt)

    return users


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    # stmt = select(User).where(User.id == user_id)
    user: User | None = await session.get(User, user_id)
    return user


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    result: Result = await session.execute(stmt)

    # return result.scalar_one()
    user: User | None = result.scalar_one_or_none()

    print("user by username", username, user)
    return user


async def update_user_partial(
    session: AsyncSession,
    user: User,
    user_update: UserUpdateSchema,
):
    for name, value in user_update.model_dump(exclude_unset=True).items():
        setattr(user, name, value)
    await session.commit()
    return user
