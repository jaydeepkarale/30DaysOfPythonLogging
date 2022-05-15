import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = RotatingFileHandler('test_rotationhandler.log', maxBytes=2000, backupCount=20)
logger.addHandler(handler)

def create_rotating_log():
    for i in range(1000):
        logger.info("This is test log line %s" % i)

if __name__ == "__main__":    
    create_rotating_log()