from time import sleep

from mysql.connector import IntegrityError
from models.link import Link
from scraper.urls.indeed_url_scraper import IndeedGbUrlScraper, IndeedUsUrlScraper
from common.logger import logger
from scraper.detail.indeed_detail_scraper import IndeedGbDetailScraper
from const.countries import Countries
from commands.harvest_urls import harvest_urls
from commands.harvest_detail import harvest_detail

logger.info(f"start cron_indeed")

indeed_gb_url_scraper =IndeedGbUrlScraper()
# indeed_us_url_scraper =IndeedUsUrlScraper()

url_scrapers = [indeed_gb_url_scraper ]

for url_scraper in url_scrapers:
    harvest_urls(url_scraper)
    
indeed_gb_detail_scraper = IndeedGbDetailScraper()
detail_scrapers = [indeed_gb_detail_scraper]

for detail_scraper in detail_scrapers:
    harvest_detail(detail_scraper)

logger.info(f"finish cron_indeed")
