import logging


logger = logging.getLogger() # this will give the instance of Logger class

logging.basicConfig(filename="day2.log", filemode="a",format="%(asctime)s--%(filename)s--%(lineno)d--%(message)s", datefmt="%Y-%m-%d", level=logging.DEBUG)

logger.info("This info mesasge will be logged to a file")
logger.error("This error mesasge will also be logged to a file")

logger.warning("Appending warning mesasge will to the file")