from const.countries import Countries, queries, link_prefixes
from scraper.urls.url_scraper import UrlScraper
from common.logger import logger
from mysql.connector import IntegrityError
from models.link import Link
from time import sleep

def save_link(link: Link):
        try:
            link.save()
        except IntegrityError as e:
            if 'Duplicate entry' in str(e):
                logger.info(f"Duplicate link. ID: {link.external_id}, Origin: {link.origin}")
            else:
                logger.error("Error on scraping indeed url country={country}, i={i}")
                logger.exception(e)
        except Exception as e:
                logger.error("Error on scraping indeed url country={country}, i={i}")
                logger.exception(e)

def harvest_urls(scraper: UrlScraper) -> None:

    for i in range(1):
        sleep(3) # sleep to not DDoS
        scraper_name = type(scraper).__name__
        logger.info(f"start scrape_url {scraper_name}, page: {i}")
        links = scraper.scrape(0)

        for link in links:
            save_link(link)
    


