import logging

from aiohttp import web

from common import configure_logging, create_url, get_api

log = logging.getLogger(__name__)

routes = web.RouteTableDef()

STOCKS_API_BASE = "https://openexchangerates.org/"
WEATHER_API_BASE = "https://api.open-meteo.com/"


@routes.get("/stocks")
async def get_stocks(request: web.Request):
    log.info("Starting processing stocks request")
    url = create_url(STOCKS_API_BASE, "/api/currencies.json")
    result = await get_api(url)
    log.info("Done processing stocks request")
    return web.json_response(data={"stocks": result})


@routes.get("/weather")
async def get_weather(request: web.Request):
    log.info("Start weather fetching")
    url = create_url(WEATHER_API_BASE, "/v1/forecast")
    result = await get_api(
        url,
        params={
            "latitude": "55.7558",
            "longitude": "37.6173",
        },
    )
    log.info("Done weather fetching")
    return web.json_response(data={"weather": result})


app = web.Application()
app.add_routes(routes)


def main():
    configure_logging()
    web.run_app(app)


if __name__ == "__main__":
    main()
