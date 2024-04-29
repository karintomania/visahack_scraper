from pathlib import Path
import os


PROJECT_PATH = str(Path(__file__).resolve().parent.parent)
# LOG_PATH = PROJECT_PATH + "/logs"

# Days to deactivate the job
JOB_EXPIRED_DAYS = int(os.getenv("JOB_EXPIRED_DAYS", 30))
# Days to remove the job from DB
JOB_REMOVAL_DAYS = int(os.getenv("JOB_REMOVAL_DAYS", 60))
# Days to remove the link from DB
LINK_REMOVAL_DAYS = int(os.getenv("LINK_REMOVAL_DAYS", 30))

SLEEP_BETWEEN_URL = int(os.getenv("SLEEP_BETWEEN_URL", 10))
SLEEP_BETWEEN_DETAILS = int(os.getenv("SLEEP_BETWEEN_DETAILS", 5))

SCRAPING_RETRY_ON_ERROR = int(os.getenv("SCRAPING_RETRY_ON_ERROR", 2))
