import os
import asyncio
import uvloop


async def run_main():
    await asyncio.sleep(1)


def main():
    if "nt" in os.name:
        asyncio.set_event_loop_policy(
            asyncio.WindowsSelectorEventLoopPolicy()
        )
    else:
        uvloop.install()
    asyncio.run(run_main())


if __name__ == '__main__':
    main()
