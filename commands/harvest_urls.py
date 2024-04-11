from const.urls import Websites
from const.countries import Countries
from scraper.urls.url_scraper import UrlScraper
from common.logger import logger
from mysql.connector import IntegrityError
from models.link import Link
from time import sleep
from const.common import SLEEP_BETWEEN_URL, SCRAPING_RETRY_ON_ERROR


target_pages = {
    Websites.INDEED: {
        Countries.GB: 3,
        Countries.US: 10,
    },
}


def save_link(link: Link):
    try:
        link.save()
    except IntegrityError as e:
        if "Duplicate entry" in str(e):
            logger.info(
                f"Duplicate link. ID: {link.external_id}, Origin: {link.origin}"
            )
        else:
            logger.error("Error on scraping indeed url country={country}, i={i}")
            logger.exception(e)
    except Exception as e:
        logger.error("Error on scraping indeed url country={country}, i={i}")
        logger.exception(e)


def harvest_urls(scraper: UrlScraper) -> None:

    scraper_name = type(scraper).__name__
    logger.info(f"start scrape_url {scraper_name}")

    end_page = target_pages[scraper.website][scraper.country]
    for i in range(end_page):
        sleep(SLEEP_BETWEEN_URL)  # sleep to not DDoS
        logger.info(f"start scrape_url {scraper_name}, page: {i}")

        counter = 0
        is_finished = False

        while SCRAPING_RETRY_ON_ERROR > counter and not is_finished:
            try:
                links = scraper.scrape(i)
                is_finished = True
            except Exception as e:
                logger.error(e)
                counter += 1

        for link in links:
            save_link(link)

    logger.info(f"finish scrape_url {scraper_name}")
