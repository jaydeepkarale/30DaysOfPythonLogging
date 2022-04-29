import yaml
import json
import logging
import logging.config

with open('Day14\config.yaml', 'r') as configyml:
    confd = yaml.safe_load(configyml)

logging.config.dictConfig(confd)
log = logging.getLogger('example2')

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
