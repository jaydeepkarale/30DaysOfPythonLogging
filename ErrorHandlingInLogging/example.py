import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
)

logger = logging.getLogger(__name__)

logger.info("Program starts")
logger.info("This %s has too many arguments", "msg", "other")
logger.info("Program is over")
