import logging
import sys

# from const.common import LOG_PATH
# from logging.handlers import TimedRotatingFileHandler
# import os

logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)

# File handler
# log_file_path = os.path.join(LOG_PATH, "myapp.log")
# handler = TimedRotatingFileHandler(
#     filename=log_file_path, when="midnight", interval=1, backupCount=30
# )
# handler.suffix = "%Y-%m-%d"

handler = logging.StreamHandler(sys.stdout)

formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)
