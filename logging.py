import logging

logging.basicConfig(level=logging.DEBUG, filename="example.log", filemode="w")

logging.debug("This is a debug message")
logging.info("This is an info")
logging.warning("This is a warning")
