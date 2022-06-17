from logging import LoggerAdapter
import logging

# get a standarad logger
logger_def = logging.getLogger('Demo Logging Adapter Class')

# in the formatter add contextual information key, in this case it's customargument
logging.basicConfig(format='%(asctime)s--%(message)s--{%(customargument)s}',level=logging.DEBUG)

# Pass the logger_def to LoggerAdapter & assign value to customargument
adapter = LoggerAdapter(logger_def, {'customargument': 'This will be appended automatically to every log'})

try: 
    logger_def.info("Attempting to do something stupid")    
    1/0
except Exception as ex:    
    logger_def.error("%s", ex)