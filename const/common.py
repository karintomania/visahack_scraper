from pathlib import Path
import sys

PROJECT_PATH = str(Path(__file__).resolve().parent.parent)
LOG_PATH = PROJECT_PATH + "/logs"

# Days to deactivate the job
JOB_EXPIRED_DAYS = 30
# Days to remove the job from DB
JOB_REMOVAL_DAYS = 60
