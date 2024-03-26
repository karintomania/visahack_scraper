import logging
from logging.handlers import TimedRotatingFileHandler
import os
from const.common import LOG_PATH

log_file_path = os.path.join(LOG_PATH, "myapp.log")

logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)

handler = TimedRotatingFileHandler(
    filename=log_file_path, when="midnight", interval=1, backupCount=30
)
handler.suffix = "%Y-%m-%d"
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
