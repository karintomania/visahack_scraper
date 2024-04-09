from pathlib import Path
import sys
import os


PROJECT_PATH = str(Path(__file__).resolve().parent.parent)
# LOG_PATH = PROJECT_PATH + "/logs"

# Days to deactivate the job
JOB_EXPIRED_DAYS = os.getenv("JOB_EXPIRED_DAYS", 30)
# Days to remove the job from DB
JOB_REMOVAL_DAYS = os.getenv("JOB_REMOVAL_DAYS", 60)

SLEEP_BETWEEN_URL = os.getenv("SLEEP_BETWEEN_URL", 10)
SLEEP_BETWEEN_DETAILS = os.getenv("SLEEP_BETWEEN_DETAILS", 5)

SCRAPING_RETRY_ON_ERROR = os.getenv("SCRAPING_RETRY_ON_ERROR", 2)
