from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.functions import count

from core.models import AccessPermission


async def check_permission(
    session: AsyncSession,
    token: str,
    action: str,
) -> bool:
    stmt = (
        select(count(AccessPermission.id))
        .where(
            AccessPermission.token == token,
            AccessPermission.action == action,
        )
        .limit(1)
    )
    total = await session.scalar(stmt)
    return bool(total)
