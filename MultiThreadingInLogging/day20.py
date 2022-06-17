import logging
import threading

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - [%(threadName)s] - %(name)s - %(funcName)s- %(message)s",
)
logger = logging.getLogger(__name__)

def worker():
    """
    Worker thread
    """
    for i in range(5):
        logger.info("log message %d from worker thread", i)

thread = threading.Thread(target=worker)
thread.start()

for i in range(5):
    logger.info("log message %d from main thread", i)

thread.join()