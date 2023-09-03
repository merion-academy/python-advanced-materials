import logging
import urllib.parse

from aiohttp import ClientSession

log = logging.getLogger(__name__)

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
    )


def create_url(base: str, path: str):
    return urllib.parse.urljoin(base, path)


async def get_api(url: str, params: dict = None) -> dict:
    async with ClientSession() as session:
        async with session.get(url, params=params) as response:
            log.info("Response url %s", response.url)
            return await response.json()
