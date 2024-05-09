from common.logger import logger
from commands.expiration_check import check_expiration
from expiration_checker.indeed_expiration_checker import IndeedExpirationChecker


logger.info("start expiration check")

checkers = [IndeedExpirationChecker()]

for checker in checkers:
    check_expiration(checker)

logger.info("finish expiration check")
