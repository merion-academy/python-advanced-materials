import asyncio
import logging

from aio_pika import connect
from aio_pika.abc import AbstractIncomingMessage

from common import configure_logging

import config

log = logging.getLogger(__name__)


async def on_message(
    message: AbstractIncomingMessage,
):
    log.info("received message %s", message)
    log.info("message body %s", message.body)

    log.info("start processing")
    await asyncio.sleep(1)
    log.info("done processing")


async def main():
    connection = await connect(config.MQ_URL)
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(config.MQ_QUEUE_NAME)

        await queue.consume(on_message, no_ack=True)

        log.info("waiting for messages, ctrl + C for exit")
        await asyncio.Future()


if __name__ == "__main__":
    configure_logging()
    asyncio.run(main())
