import asyncio

from aio_pika import connect, Message
from aio_pika.abc import AbstractChannel, AbstractQueue
import config


async def create_task(
    message: bytes,
    channel: AbstractChannel,
    queue: AbstractQueue,
):
    await channel.default_exchange.publish(
        Message(message),
        routing_key=queue.name,
    )


async def main():
    connection = await connect(config.MQ_URL)

    async with connection:
        channel = await connection.channel()

        queue = await channel.declare_queue(
            config.MQ_QUEUE_NAME,
        )

        async with asyncio.TaskGroup() as tg:
            tg.create_task(
                create_task(
                    b"hello again",
                    channel=channel,
                    queue=queue,
                ),
            )
            tg.create_task(
                create_task(
                    b"another hello",
                    channel=channel,
                    queue=queue,
                ),
            )


if __name__ == "__main__":
    asyncio.run(main())
