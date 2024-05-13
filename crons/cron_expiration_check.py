from common.logger import logger
from commands.expiration_check import check_expiration
from expiration_checker.indeed_expiration_checker import IndeedExpirationChecker
from expiration_checker.reed_expiration_checker import ReedExpirationChecker


logger.info("start expiration check")

checkers = [
    IndeedExpirationChecker(),
    ReedExpirationChecker(),
]

for checker in checkers:
    check_expiration(checker)

logger.info("finish expiration check")
