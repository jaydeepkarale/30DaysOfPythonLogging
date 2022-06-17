from logging import LoggerAdapter
import logging
from logging import LogRecord


class FilterThis(logging.Filter):
    def filter(self, record: LogRecord) -> bool:
        return'SECRET'not in record.msg


# get a standarad logger
logging.basicConfig(format='%(asctime)s--%(message)s',level=logging.DEBUG)
logger_def = logging.getLogger('Demo Logging Adapter Class')
logger_def.addFilter(FilterThis())

try: 
    logger_def.info("Attempting to do something stupid SECRET")        
    1/0
except Exception as ex:    
    logger_def.error("%s", ex)