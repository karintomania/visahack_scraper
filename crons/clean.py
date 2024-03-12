from cleaner.clean_query import deactivate_jobs, clean_links
from common.logger import logger

print("running!")
logger.info("Start cleaning")

# deactivate jobs
try:
    row_count = deactivate_jobs()

    logger.info(f"{row_count} jobs deactivated")
except Exception as e:
    logger.error("Error on deactivating jobs")
    logger.exception(e)

# clean links
try:
    row_count = clean_links()
    logger.info(f"{row_count} links cleaned")
except Exception as e:
    logger.error("Error on cleaning links")
    logger.exception(e)
 
logger.info("Finished cleaning")
