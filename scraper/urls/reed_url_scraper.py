from typing import List
from models.link import Link
from scraper.read_html import read_html
from bs4 import BeautifulSoup
from scraper.urls.url_scraper import UrlScraper
from const.countries import Countries
from const.urls import Websites, link_prefixes


class ReedUrlScraper(UrlScraper):
    def __init__(self, country=Countries.GB):
        super().__init__(Websites.REED, country)

    def scrape(self, url: str) -> List[Link]:
        html_source = read_html(url)

        result = self.get_list(html_source)

        return result

    def get_list(self, html: str) -> List[Link]:
        soup = BeautifulSoup(html, "html.parser")
        urls: List[Link] = []
        articles = soup.find("main").find_all("article")

        for article in articles:
            job_header = article.find("h2")

            link = job_header.find("a").get("href")

            job_title = job_header.text

            external_id = article.get("data-id")

            job_link = Link(
                external_id=external_id,
                origin=Websites.REED.value,
                url=link,
                country=self.country.value,
            )

            urls.append(job_link)

        return urls


class ReedGbUrlScraper(ReedUrlScraper):
    def __init__(self):
        super().__init__(Countries.GB)


class ReedUsUrlScraper(ReedUrlScraper):
    def __init__(self):
        super().__init__(Countries.US)
