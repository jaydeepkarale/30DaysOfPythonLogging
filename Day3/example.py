import logging


logger = logging.getLogger() # this will give the instance of Logger class

logging.basicConfig(format="%(asctime)s--%(filename)s--%(levelname)s--%(lineno)d--%(message)s", datefmt="%Y-%m-%d", level=logging.DEBUG)

def return_sum_of_two_numbers(a, b):
    logger.info("Inside function to add %d %d", a, b)
    try:
        logger.warning("There are no checks if the inputs are integers")
        return a + b
    except Exception as ex:
        logger.error("%s", ex)


print(return_sum_of_two_numbers(10,20))

print(return_sum_of_two_numbers(10,'a'))