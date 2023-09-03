from typing import Literal, Annotated

from fastapi import HTTPException, status, Security
from fastapi.security import APIKeyHeader

from cruds.permissions import check_permission

access_token = APIKeyHeader(name="access_token")


class PermissionRequired:
    def __init__(self, action: str):
        self.action = action

    async def __call__(
        self,
        token: Annotated[str, Security(access_token)],
    ) -> Literal[True]:
        allowed: bool = await check_permission(
            token=token,
            action=self.action,
        )
        if allowed:
            return True

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            # detail=
        )
