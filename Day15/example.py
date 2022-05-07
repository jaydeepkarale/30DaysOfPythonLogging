import logging
from pythonjsonlogger import jsonlogger


logger = logging.getLogger()

logHandler = logging.FileHandler(filename="./example.log")
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

logging.basicConfig(level=logging.DEBUG, format='%(message)s\n')
try:
    
    1/0
except Exception as ex:    
    logging.error("%s\n", ex, exc_info=True)