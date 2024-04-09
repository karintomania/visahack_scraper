from pathlib import Path
import sys
import os

PROJECT_PATH = str(Path(__file__).resolve().parent.parent)
# LOG_PATH = PROJECT_PATH + "/logs"

# Days to deactivate the job
JOB_EXPIRED_DAYS = os.getenv("JOB_EXPIRED_DAYS", 30)
# Days to remove the job from DB
JOB_REMOVAL_DAYS = os.getenv("JOB_REMOVAL_DAYS", 60)

# Indeed pages to scrape
INDEED_SCRAPE_PAGES = os.getenv("INDEED_SCRAPE_PAGES", 3)
