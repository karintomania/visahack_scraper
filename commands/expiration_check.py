from time import sleep

from common.logger import logger
from const.common import SLEEP_BETWEEN_URL
from expiration_checker.expiration_checker import ExpirationChecker
from expiration_checker.indeed_expiration_checker import IndeedExpirationChecker
from models.job import Job


def check_expiration(checker: ExpirationChecker):
    checker_name = type(checker).__name__
    logger.info(f"start expiration check: {checker_name}")

    jobs_to_check = Job.get_expiration_check_target(checker.website)

    for job in jobs_to_check:
        sleep(SLEEP_BETWEEN_URL)
        try:
            is_url_expired = checker.is_url_expired(job.url)

            if is_url_expired:
                logger.info(f"Expired job id: {job.id}")
                job.active = False
                job.save()

        except Exception as e:
            logger.error(
                f"Error on checking expiration on: {checker_name}, job: {job.id}"
            )
            logger.exception(e)

    pass
