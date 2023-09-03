from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from .schemas import UserSchema, UserSchemaIn
from . import crud

router = APIRouter(tags=["Users"])


@router.get("/", response_model=list[UserSchema])
async def get_users_list(
    session: AsyncSession = Depends(db_helper.get_session_dependency),
):
    return await crud.get_users(session=session)


@router.post("/", response_model=UserSchema)
async def create_user(
    data_create: UserSchemaIn,
    session: AsyncSession = Depends(db_helper.get_session_dependency),
):
    return await crud.create_user(
        session=session,
        user_create=data_create,
    )


@router.get("/{user_id}/", response_model=UserSchema)
async def get_user_by_id(
    user_id: int,
    session: AsyncSession = Depends(db_helper.get_session_dependency),
):
    user = await crud.get_user_by_id(
        session=session,
        user_id=user_id,
    )
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found!",
    )

