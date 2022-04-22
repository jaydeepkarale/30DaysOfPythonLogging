import logging
import logging.config
from os import path


logging.config.fileConfig('logging.ini')

# create logger
logger = logging.getLogger('eample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')