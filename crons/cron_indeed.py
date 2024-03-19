from time import sleep

from mysql.connector import IntegrityError
from models.link import Link
from scraper.urls.indeed_url_scraper import IndeedUrlScraper
from common.logger import logger
from scraper.detail.indeed_detail_scraper import IndeedDetailScraper


def scrape_urls():
    ius = IndeedUrlScraper()

    for i in range(1):
        sleep(10)
        country = "GB"
        links = ius.scrape(country, i)
        logger.info(f"start cron_indeed#scrape_urls. country:{country}, page:{i}")
        for link in links:
            try:
                link.save()
            except IntegrityError as e:
                if 'Duplicate entry' in str(e):
                    logger.info(f"Duplicate link. ID: {link.external_id}, Origin: {link.origin}")
                else:
                    logger.error("Error on scraping indeed url country={country}, i={i}")
                    logger.exception(e)
                    break
            except Exception as e:
                    logger.error("Error on scraping indeed url country={country}, i={i}")
                    logger.exception(e)
                    break


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

scrape_urls()

scrape_details()

