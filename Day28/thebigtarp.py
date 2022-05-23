try:
    main_loop()
except Exception:
    logger.exception("Fatal error in main loop")