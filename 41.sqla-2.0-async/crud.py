import asyncio
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from models import User, Post

import config


async def create_user(
    session: AsyncSession,
    username: str,
    email: str = "",
    motto: str | None = None,
) -> User:
    user = User(
        username=username,
        email=email,
        motto=motto,
    )
    print("new user", user)
    async with session.begin():
        session.add(user)
    print("created user", user)
    return user


async def get_users(session: AsyncSession) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result = await session.execute(stmt)
    users = result.scalars().all()
    for user in users:
        print(user)
    print(users)

    return users


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    # stmt = select(User).where(User.id == user_id)
    user: User | None = await session.get(User, user_id)
    print("user", user_id, user)
    return user


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    result: Result = await session.execute(stmt)

    # return result.scalar_one()
    user: User | None = result.scalar_one_or_none()

    print("user by username", username, user)
    return user


async def create_posts_for_user(
    session: AsyncSession,
    user: User,
    *post_titles: str,
) -> list[Post]:
    posts = [
        Post(title=title, author_id=user.id)
        for title in post_titles
    ]
    print(posts)
    async with session.begin_nested():
        session.add_all(posts)

    # print("saved posts", posts)
    for post in posts:
        print(post)

    return posts


async def get_posts_with_users(session: AsyncSession):
    stmt = (
        select(Post)
        .options(
            joinedload(Post.author)
        )
        .order_by(Post.id)
    )
    result: Result = await session.execute(stmt)
    posts = result.scalars().all()
    print(posts)
    for post in posts:
        print("=" * 7, post)
        print("+", post.author)

    return posts


async def get_users_with_posts(session: AsyncSession):
    stmt = (
        select(User)
        .options(
            # to-one (or to-many + unique)
            # joinedload(User.posts)
            selectinload(User.posts)
        )
        .order_by(User.id)
    )
    result: Result = await session.execute(stmt)
    # users = result.unique().scalars().all()
    users = result.scalars().all()
    for user in users:
        print("=" * 10, user)
        for post in user.posts:
            print("---", post)
    return users


async def main():
    async_engine = create_async_engine(
        url=config.DB_URL,
        echo=config.DB_ECHO,
    )
    async_session = async_sessionmaker(
        async_engine,
        expire_on_commit=False,
    )

    async with async_session() as session:
        await create_user(
            session,
            "john",
        )
        await create_user(
            session,
            "sam",
            email="sam@example.com",
        )
        await create_user(
            session,
            "nick",
            motto="some motto",
        )
        await create_user(
            session,
            "alice",
            email="alice@example.com",
        )
        await create_user(
            session,
            "bob",
            motto="some motto",
        )
        await get_users(session)
        await get_user_by_id(session, 1)
        await get_user_by_id(session, 2)
        await get_user_by_id(session, 0)
        sam: User = await get_user_by_username(session, "sam")
        john: User = await get_user_by_username(session, "john")
        await get_user_by_username(session, "bob")

        await create_posts_for_user(session, sam, "P1", "P2")
        await create_posts_for_user(session, john, "J1", "J2", "J3")
        await get_posts_with_users(session)
        await get_users_with_posts(session)


if __name__ == "__main__":
    asyncio.run(main())
