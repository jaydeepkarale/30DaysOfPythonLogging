try:
    something()
except SomeError as err:
    logger.warn("...")
    raise DifferentError() from err