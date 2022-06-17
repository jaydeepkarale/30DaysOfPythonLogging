# package/
# │
# ├── __init__.py
# └── module1.py

# __init__.py
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

# module1.py
logger = logging.getLogger(__name__)
logger.info("this is an info log message")