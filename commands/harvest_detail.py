from const.countries import Countries, queries, link_prefixes
from scraper.detail.detail_scraper import DetailScraper
from common.logger import logger
from models.job import Job
from models.link import Link
from time import sleep


def harvest_detail(scraper: DetailScraper) -> None:

    scraper_name = type(scraper).__name__
    logger.info(f"start scrape_detail {scraper_name}")

    links = Link.find_no_details()
    for link in links:
        logger.info(f"start scrape_detail {link.origin}, {link.country}, {link.external_id}")
        sleep(5)
        try:
            result = scraper.scrape(link)
            result.save()
            link.has_detail = True
            link.save()
        except Exception as e:
            logger.error("Error on scraping indeed details link id={link.id}")
            logger.exception(e)
            break
    


