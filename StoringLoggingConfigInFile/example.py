import logging
import logging.config
from os import path


logging.config.fileConfig('StoringLoggingConfigInFile\logging.ini')

# create logger
logger = logging.getLogger('example')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')