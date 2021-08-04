import logging

logging.basicConfig(
    filename="log.txt",
    format='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s',
    level=10,
    filemode="w",
    datefmt='%m/%d/%Y %I:%M:%S'
)
logging.debug("This is a debug level log")
logging.info("This is a info level log")
logging.warning("This is a warning level log")
logging.error("This is a error level log")
logging.critical("This is a critical level log")
