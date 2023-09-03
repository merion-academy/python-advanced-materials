"""
token a 'be335ca4-ab47-4fd5-947a-35120210ddbb'
token b 'dfd56867-b0f4-4382-8559-4ead85224ff3'
"""

import asyncio

from core.models import db_helper
from core.models.access_permission import generate_token, AccessPermission


async def main():
    async with db_helper.async_session() as session:
        async with session.begin():
            access_read_users_a = AccessPermission(action="USERS_GET")
            access_read_users_b = AccessPermission(
                token=generate_token(),
                action="USERS_GET",
            )
            access_write_users = AccessPermission(
                token=access_read_users_b.token,
                action="USER_CREATE",
            )
            session.add_all(
                [
                    access_read_users_a,
                    access_read_users_b,
                    access_write_users,
                ]
            )

    print("token a", repr(access_read_users_a.token))
    print("token b", repr(access_read_users_b.token))


if __name__ == "__main__":
    asyncio.run(main())
