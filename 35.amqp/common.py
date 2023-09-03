import logging


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(funcName)15s %(module)s:%(lineno)d %(levelname)-8s - %(message)s",
    )
