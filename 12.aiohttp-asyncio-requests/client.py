import asyncio
import logging

from common import configure_logging, create_url, get_api

log = logging.getLogger(__name__)

API_BASE = "http://0.0.0.0:8080"


def api_url(path: str):
    return create_url(API_BASE, path)


async def run_main():
    log.info("Run API calls")
    async with asyncio.TaskGroup() as tg:
        task_stocks = tg.create_task(get_api(api_url("/stocks")))
        task_weather = tg.create_task(get_api(api_url("/weather")))

    log.info("Stocks: %s", task_stocks.result())
    log.info("Weather: %s", task_weather.result())


def main():
    configure_logging()
    asyncio.run(run_main())


if __name__ == '__main__':
    main()
