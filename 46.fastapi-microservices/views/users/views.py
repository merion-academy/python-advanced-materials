from typing import Annotated
from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession

from common.dependencies import PermissionRequired
from core.models import db_helper, User
from utils.email_sender import send_email
from .dependencies import get_user_by_id_or_raise
from .schemas import UserSchema, UserCreateSchema, UserUpdateSchema
from . import crud


router = APIRouter(tags=["Users"])


@router.get("/", response_model=list[UserSchema])
async def get_users_list(
    session: Annotated[AsyncSession, Depends(db_helper.get_session_dependency)],
    _: bool = Depends(PermissionRequired("USERS_GET")),
):
    return await crud.get_users(session=session)


@router.post(
    "/",
    response_model=UserSchema,
    dependencies=[
        Depends(PermissionRequired("USER_CREATE")),
    ]
)
async def create_user(
    background_tasks: BackgroundTasks,
    # session: Annotated[AsyncSession, Depends(db_helper.get_session_dependency)],
    data_create: UserCreateSchema,
    session: AsyncSession = Depends(db_helper.get_session_dependency),
):
    user = await crud.create_user(
        session=session,
        user_create=data_create,
    )
    background_tasks.add_task(
        send_email,
        user.email,
        f"Hello dear {user.username}",
        text="Welcome message.",
    )
    return user


@router.get("/{user_id}/", response_model=UserSchema)
async def get_user_by_id(
    user: User = Depends(get_user_by_id_or_raise),
):
    return user


@router.patch("/{user_id}/", response_model=UserSchema)
async def update_user_partial(
    data_update: UserUpdateSchema,
    user: User = Depends(get_user_by_id_or_raise),
    session: AsyncSession = Depends(db_helper.get_session_dependency),
):
    return await crud.update_user_partial(
        session=session,
        user=user,
        user_update=data_update,
    )
