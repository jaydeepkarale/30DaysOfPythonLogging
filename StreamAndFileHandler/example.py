import logging
from stat import filemode

# create logger
logger = logging.getLogger('example_for_handlers')
logger.setLevel(logging.DEBUG)

# create a stream & file handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename='StreamAndFileHandler/log.txt', mode='w')

# create a common formatter 
formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s-%(name)s')

# add formatter to both handlers
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# set streamhandler default level to DEBUG
stream_handler.setLevel(logging.DEBUG)

# set filehandler default to ERROR
file_handler.setLevel(logging.ERROR)

# add handler to logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# write logs
logger.debug("This debug log will only be written to console")
logger.info("This info log will only be written to console")
logger.error("This error log will be written to console & file")
logger.critical("This critical log will be written to console & file")