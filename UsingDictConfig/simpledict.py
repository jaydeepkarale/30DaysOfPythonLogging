import json
import logging
import logging.config

confd = dict({
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default_formatter": {
            "format": "[%(levelname)s:%(asctime)s:%(module)s] %(message)s"
        },
    },
    "handlers": {
        "stream_handler": {
            "class": "logging.StreamHandler",
            "formatter": "default_formatter",
        },
    },
    "loggers": {
        "": {
            "handlers": ["stream_handler"],
            "level": "INFO",
            "propagate": True
        }
    }
}
)
logging.config.dictConfig(confd)
log = logging.getLogger(__name__)

def add_two_numbers(a: int, b: int):
    log.warning(f"Consider adding check for input to be integers")
    
    log.info(f"Adding {a} & {b}")
    try:
        print(a + b)
    except Exception as ex:
        log.error("%s", ex)

if __name__ == '__main__':
    add_two_numbers(10,20)
    add_two_numbers(10,'a')