import logging
from functools import wraps
from timeit import default_timer

logger = logging.getLogger(__name__)


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(funcName)15s %(module)7s:%(lineno)d %(levelname)-6s - %(message)s",
    )


def timer(func):
    @wraps(func)
    def wrapper(*a, **kw):
        start_time = default_timer()
        result = func(*a, **kw)
        total_time = default_timer() - start_time
        logger.info(
            "Func %s call total time %.3f",
            func.__name__,
            total_time,
        )
        return result

    return wrapper
