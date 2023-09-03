from aiohttp import ClientSession

from config import settings


async def check_permission(
    token: str,
    action: str,
) -> bool:
    permission_check_data = {
        "token": token,
        "action": action,
    }
    async with ClientSession() as session:
        async with session.post(
            url=settings.permissions.url,
            json=permission_check_data,
        ) as response:
            data: dict = await response.json()
            return bool(data.get("allow"))
