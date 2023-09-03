from typing import Sequence

from sqlalchemy import create_engine, select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session, joinedload, selectinload

from models import User, Post

import config


def create_user(
    session: Session,
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
    session.add(user)
    session.commit()
    print("created user", user)
    return user


def get_users(session: Session) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result = session.execute(stmt)
    users = result.scalars().all()
    for user in users:
        print(user)
    print(users)

    return users


def get_user_by_id(session: Session, user_id: int) -> User | None:
    # stmt = select(User).where(User.id == user_id)
    user: User | None = session.get(User, user_id)
    print("user", user_id, user)
    return user


def get_user_by_username(session: Session, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    result: Result = session.execute(stmt)

    # return result.scalar_one()
    user: User | None = result.scalar_one_or_none()

    print("user by username", username, user)
    return user


def create_posts_for_user(
    session: Session,
    user: User,
    *post_titles: str,
) -> list[Post]:
    posts = [
        Post(title=title, author_id=user.id)
        for title in post_titles
    ]
    print(posts)
    session.add_all(posts)
    session.commit()
    # print("saved posts", posts)
    for post in posts:
        print(post)

    return posts


def get_posts_with_users(session: Session):
    stmt = (
        select(Post)
        .options(joinedload(Post.author))
        .order_by(Post.id)
    )
    result = session.execute(stmt)
    posts = result.scalars().all()
    print(posts)
    for post in posts:
        print("=" * 7, post)
        print("+", post.author)

    return posts


def get_users_with_posts(session: Session):
    stmt = (
        select(User)
        .options(
            # to-one (or to-many + unique)
            # joinedload(User.posts)
            selectinload(User.posts)
        )
        .order_by(User.id)
    )
    result = session.execute(stmt)
    # users = result.unique().scalars().all()
    users = result.scalars().all()
    for user in users:
        print("=" * 10, user)
        for post in user.posts:
            print("---", post)
    return users


def main():
    engine = create_engine(
        url=config.DB_URL,
        echo=config.DB_ECHO,
    )
    with Session(engine) as session:
        create_user(
            session,
            "john",
        )
        create_user(
            session,
            "sam",
            email="sam@example.com",
        )
        create_user(
            session,
            "nick",
            motto="some motto",
        )
        get_users(session)
        get_user_by_id(session, 1)
        get_user_by_id(session, 2)
        get_user_by_id(session, 0)
        sam = get_user_by_username(session, "sam")
        john = get_user_by_username(session, "john")
        get_user_by_username(session, "bob")

        create_posts_for_user(session, sam, "P1", "P2")
        create_posts_for_user(session, john, "J1", "J2", "J3")
        get_posts_with_users(session)
        get_users_with_posts(session)


if __name__ == "__main__":
    main()
