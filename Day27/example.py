import logging

logger = logging.getLogger('demo_logger')
logging.basicConfig(level=logging.DEBUG)


def check_status(status):
    if status == "Open":
        logger.debug("Good status")
    else:
        logger.error("Unknown status: {0}".format(status))


if __name__ == '__main__':
    check_status("Open")



