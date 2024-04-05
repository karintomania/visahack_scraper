from time import sleep

from mysql.connector import IntegrityError
from models.link import Link
from scraper.urls.indeed_url_scraper import IndeedGbUrlScraper
from common.logger import logger
from scraper.detail.indeed_detail_scraper import IndeedDetailScraper
from const.countries import Countries
from commands.harvest_urls import harvest_urls

def scrape_details():
    ids = IndeedDetailScraper()
    links = Link.find_no_details()
    logger.info(f"start cron_indeed#scrape_details.")

    for link in links:
        sleep(5)
        try:
            result = ids.scrape(link)
            result.save()
            link.has_detail = True
            link.save()
        except Exception as e:
            logger.error("Error on scraping indeed details link id={link.id}")
            logger.exception(e)
            break


logger.info(f"start cron_indeed")

gb_indeed_url_scraper =IndeedGbUrlScraper()

url_scrapers = [gb_indeed_url_scraper]

for url_scraper in url_scrapers:
    harvest_urls(url_scraper)
    

# scrape_details()
