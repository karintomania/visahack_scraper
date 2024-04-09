from const.countries import Countries
from scraper.detail.detail_scraper import DetailScraper
from common.logger import logger
from models.job import Job
from models.link import Link
from time import sleep
from scraper.detail.no_sponsor_exception import NoSponsorException


def harvest_details(scraper: DetailScraper) -> None:

    scraper_name = type(scraper).__name__
    logger.info(f"start scrape_detail {scraper_name}")

    links = Link.find_no_details(scraper.website, scraper.country)

    for link in links:
        logger.info(f"start scrape_detail {link.origin}, {link.country}, {link.external_id}")
        sleep(5)
        try:
            result = scraper.scrape(link)
            result.save()
            link.has_detail = True
            link.save()
        except NoSponsorException as e:
            logger.info(f"No Sponsorship on the link: link id={link.id}")
            continue
        except Exception as e:
            logger.error(f"Error on scraping indeed details link id={link.id}")
            logger.exception(e)
            break

    logger.info(f"finish scrape_detail {scraper_name}")

    


