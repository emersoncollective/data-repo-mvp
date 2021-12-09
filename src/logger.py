from datetime import datetime
import logging
import os
import sys
import time


def create_and_return_logger(logger_name, filename="log"):
    """
    Function to create a custom logger that will print to terminal
        as well as write to a log file
    Accepts: Logger name for script that is calling logger, and filename for log.
    Returns: Logger object and Log file path.
    """
    LOG_FILE_DIR = os.getcwd() + "/logs"
    if not os.path.exists(LOG_FILE_DIR):
        os.makedirs(LOG_FILE_DIR)

    LOG_FILE = f"{LOG_FILE_DIR}/{filename}_{datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d_%H_%M_%S')}.log"

    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.DEBUG)
    logFormatter = logging.Formatter(
        "%(levelname)s %(asctime)s %(processName)s %(message)s"
    )

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(logFormatter)

    logger.handlers.clear()
    logger.addHandler(sh)

    fileHandler = logging.FileHandler(f"{LOG_FILE}")
    fileHandler.setFormatter(logFormatter)

    logger.addHandler(fileHandler)
    return logger, LOG_FILE
