import logging
import multiprocessing
import os

logging.basicConfig(
    level=logging.INFO,
    datefmt="%H:%M:%S",
    format="%(asctime)s.%(msecs)03d %(funcName)15s:%(lineno)-3d - %(message)s",
)

log = logging.getLogger(__name__)


timeout = 64_000_000


def countdown(n):
    log.info("countdown to %s", n)
    while n:
        n -= 1
    log.info("done countdown")


# def main():
#     log.info("start main")
#     # countdown(timeout)
#     process = multiprocessing.Process(
#         target=countdown,
#         args=(timeout, ),
#     )
#     log.info("created process, starting")
#     process.start()
#     log.info("started process, joining")
#     process.join()
#
#     log.info("done main")


def two_procs():
    log.info("start main")
    # countdown(timeout)
    proc_1 = multiprocessing.Process(
        target=countdown,
        args=(timeout,),
    )
    proc_2 = multiprocessing.Process(
        target=countdown,
        args=(timeout,),
    )
    log.info("created processes, starting")
    procs = [proc_1, proc_2]
    for proc in procs:
        proc.start()
    log.info("started processes, joining")
    for proc in procs:
        proc.join()

    log.info("done main")


def main_countdowns():
    log.info("start main")

    timeouts = [timeout + i for i in range(100, 1000, 250)]
    with multiprocessing.Pool() as pool:
        pool.map(countdown, timeouts)

    log.info("done main")


def fac(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main_fac():
    log.info("start main")

    nums = [10, 42, 57]
    with multiprocessing.Pool() as pool:
        factorials = pool.map(fac, nums)

    log.info("factorials: %s", factorials)

    log.info("done main")


def show_info(caller):
    log.info("info for %s", caller)
    log.info("[%s] where am I? : %s", caller, __name__)
    log.info("[%s] my process id (PID) %s", caller, os.getpid())
    log.info("[%s] parent process id (PID) %s", caller, os.getppid())


def cpu_expensive(extra_arg):
    log.info("run in func, arg = %s", extra_arg)
    show_info("cpu expensive task")


def main():
    log.info("start main")

    show_info("main")

    process = multiprocessing.Process(
        target=cpu_expensive,
        args=("qwerty",),
    )
    process.start()
    process.join()

    log.info("done main")


if __name__ == "__main__":
    main()
