try:
    something()
except SomeError:
    logger.warn("...")
    raise