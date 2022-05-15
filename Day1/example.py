import logging


logger = logging.getLogger() # this will give the instance of Logger class

logging.basicConfig(format="%(asctime)s--%(filename)s--%(lineno)d--%(message)s", datefmt="%Y-%m-%d", level=logging.DEBUG)

logger.debug("This is an debug message")
logger.info("This is an info message")



# def add_two_numbers(a, b):
#     print("I am in function to add two numbers")
#     return a + b

# print(add_two_numbers(10,20))