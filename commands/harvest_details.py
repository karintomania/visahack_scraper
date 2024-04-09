from const.countries import Countries
from scraper.detail.detail_scraper import DetailScraper
from common.logger import logger
from models.job import Job
from models.link import Link
from time import sleep
from scraper.detail.no_sponsor_exception import NoSponsorException
from const.common import SLEEP_BETWEEN_DETAILS, SCRAPING_RETRY_ON_ERROR


def harvest(scraper: DetailScraper, scraper_name: str) -> bool:

    links = Link.find_no_details(scraper.website, scraper.country)

    valid_link_count = 0

    for link in links:
        logger.info(f"start scrape_detail {link.id}, {link.origin}, {link.country}, {link.external_id}")
        sleep(SLEEP_BETWEEN_DETAILS)
        try:
            result = scraper.scrape(link)
            result.save()
            link.has_detail = True
            link.save()
            valid_link_count += 1
        except NoSponsorException as e:
            logger.info(f"No Sponsorship on the link: link id={link.id}")
            # mark these links as has_detail
            link.has_detail = True
            link.save()
            continue
        except Exception as e:
            logger.error(f"Error on scraping indeed details link id={link.id}")
            logger.exception(e)
            break

    logger.info(f"Finish scrape_detail {scraper_name}. Harvested {valid_link_count} valid inks out of {len(links)} links.")

def harvest_details(scraper: DetailScraper) -> None:

    scraper_name = type(scraper).__name__
    logger.info(f"start scrape_detail {scraper_name}")

    counter = 0
    is_finished = False

    while SCRAPING_RETRY_ON_ERROR > counter and not is_finished:
        try:
            harvest(scraper, scraper_name)
            is_finished = True
        except Exception as e:
            logger.exception(e)
            counter += 1




