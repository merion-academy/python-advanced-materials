import logging
from time import sleep
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import multiprocessing

import requests

from common import configure_logging, timer

logger = logging.getLogger(__name__)


def get_users():
    logger.info("start get users")
    sleep(1)
    logger.info("done get users")


def get_posts():
    logger.info("start get posts")
    sleep(1)
    logger.info("done get posts")


def get_user(user_id):
    logger.info("get user %s", user_id)
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}",
    )
    result = response.json()
    logger.info("got user %s", result)
    return result


def cpu_expensive(timeout):
    logger.info("countdown to %s", timeout)
    while timeout:
        timeout -= 1
    logger.info("done countdown")


@timer
def demo_threading():
    logger.info("start demo threading")
    # 1
    # get_users()
    # get_posts()

    # 2
    # thread_users = Thread(target=get_users)
    # thread_posts = Thread(target=get_posts)
    # logger.info("created threads, starting")
    # thread_users.start()
    # thread_posts.start()
    # logger.info("started threads, joining")
    # thread_users.join()
    # thread_posts.join()

    # 3
    # with ThreadPoolExecutor() as executor:
    #     executor.submit(get_users)
    #     executor.submit(get_posts)

    # 4
    # for user_id in range(1, 11):
    #     get_user(user_id)

    # 5
    # with ThreadPoolExecutor() as executor:
    #     executor.map(get_user, range(1, 11))

    # 6
    # cpu_expensive(64_000_000)
    # cpu_expensive(72_000_000)

    # 7
    # with ThreadPoolExecutor() as executor:
    #     executor.submit(cpu_expensive, 64_000_000)
    #     executor.submit(cpu_expensive, 72_000_000)

    logger.info("done demo threading")


@timer
def demo_multiprocessing():
    logger.info("start demo multiprocessing")
    # process_1 = multiprocessing.Process(
    #     target=cpu_expensive,
    #     args=(64_000_000,),
    # )
    # process_2 = multiprocessing.Process(
    #     target=cpu_expensive,
    #     args=(72_000_000,),
    # )
    # logger.info("created procs, starting")
    # process_1.start()
    # process_2.start()
    # logger.info("started procs, joining")
    # process_1.join()
    # process_2.join()
    with multiprocessing.Pool() as pool:
        pool.map(cpu_expensive, [64_000_000, 72_000_000])

    logger.info("start demo multiprocessing")


def main():
    configure_logging()
    logger.info("start main")
    # demo_threading()
    demo_multiprocessing()
    logger.info("done main")


if __name__ == "__main__":
    main()
