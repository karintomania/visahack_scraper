from time import sleep

from mysql.connector import IntegrityError
from models.link import Link
from scraper.urls.indeed_url_scraper import IndeedGbUrlScraper, IndeedUsUrlScraper
from common.logger import logger
from scraper.detail.indeed_detail_scraper import IndeedGbDetailScraper, IndeedUsDetailScraper
from const.countries import Countries
from commands.harvest_urls import harvest_urls
from commands.harvest_details import harvest_details

logger.info(f"start cron_indeed")

url_scrapers = [
    # IndeedGbUrlScraper(),
    IndeedUsUrlScraper(),
]

# for url_scraper in url_scrapers:
#     harvest_urls(url_scraper)
    
detail_scrapers = [
    # IndeedGbDetailScraper(),
    IndeedUsDetailScraper(),
]

for detail_scraper in detail_scrapers:
    harvest_details(detail_scraper)

logger.info(f"finish cron_indeed")
