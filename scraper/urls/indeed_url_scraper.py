from typing import List
from models.job import Job
from models.link import Link
from scraper.read_html import read_html
from bs4 import BeautifulSoup
from scraper.urls.url_scraper import UrlScraper
from const.countries import Countries
from const.urls import Websites, link_prefixes, queries


class IndeedUrlScraper(UrlScraper):

    def __init__(self, country = Countries.GB):
        super().__init__(Websites.INDEED, country)

    def scrape(self, page: int) -> List[Link]:

        start_index = page * 10
        url = queries[self.website][self.country].format(start_index)

        html_source = read_html(url)

        result = self.get_list(html_source)

        return result

    def get_list(self, html: str) -> List[Link]:
        soup = BeautifulSoup(html, "html.parser")
        urls: List[Link] = []
        beacons = soup.find_all(class_="job_seen_beacon")

        for beacon in beacons:
            job_data = beacon.find("table")
            job_title = job_data.find("h2")
            uri = job_title.find("a").get("href")
            link = link_prefixes[self.website][self.country].format(uri)
            external_id = job_title.find("a").get("data-jk")

            job_link = Link(
                external_id=external_id, origin="indeed", url=link, country=self.country.value
            )
            urls.append(job_link)

        return urls


class IndeedGbUrlScraper(IndeedUrlScraper):
    def __init__(self):
        super().__init__(Countries.GB)

class IndeedUsUrlScraper(IndeedUrlScraper):
    def __init__(self):
        super().__init__(Countries.US)
        
