from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import CheckPermissionRequest, CheckPermissionResponse

router = APIRouter(tags=["Access Permissions"])


@router.post(
    "/check/",
    response_model=CheckPermissionResponse,
    response_model_exclude_none=True,
)
async def check_permission(
    check_request: CheckPermissionRequest,
    session: AsyncSession = Depends(db_helper.get_session_dependency),
):
    allowed = await crud.check_permission(
        session=session,
        token=check_request.token,
        action=check_request.action,
    )
    return CheckPermissionResponse(
        allow=allowed,
        reason=None if allowed else "no access",
    )
