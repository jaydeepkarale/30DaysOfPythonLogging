import logging
import traceback

logging.basicConfig(format='%(asctime)s | %(levelname)s | %(message)s')
try:
    1/0
except Exception as ex:
    logging.error("%s %s", ex, traceback.format_exc())