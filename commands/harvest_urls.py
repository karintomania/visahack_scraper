from time import sleep
from mysql.connector import IntegrityError
from common.logger import logger
from const.common import SLEEP_BETWEEN_URL, SCRAPING_RETRY_ON_ERROR
from const.countries import Countries
from const.urls import Websites
from models.link import Link
from scraper.urls.url_generator import generate_url
from scraper.urls.url_scraper import UrlScraper
from commands.check_duplication import has_duplication


def save_link(link: Link):
    # Check duplication
    if has_duplication(link.external_id):
        logger.info(f"Duplicate link. ID: {link.external_id}, Origin: {link.origin}")
        return

    try:
        link.save()
    except Exception as e:
        logger.error("Error on scraping indeed url country={country}, i={i}")
        logger.exception(e)


def harvest_urls(scraper: UrlScraper) -> None:
    scraper_name = type(scraper).__name__
    logger.info(f"start scrape_url {scraper_name}")

    urls = generate_url(scraper.website, scraper.country)

    for url in urls:
        sleep(SLEEP_BETWEEN_URL)  # sleep to not DDoS
        logger.info(f"start scrape_url {scraper_name}, {url}")

        counter = 0
        is_finished = False

        links = []
        while SCRAPING_RETRY_ON_ERROR > counter and not is_finished:
            try:
                links = scraper.scrape(url)
                is_finished = True
            except Exception as e:
                logger.error(e)
                counter += 1

        if links:
            for link in links:
                save_link(link)

    logger.info(f"finish scrape_url {scraper_name}")
