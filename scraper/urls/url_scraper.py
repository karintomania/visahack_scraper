from typing import List
from models.link import Link
from const.countries import Countries
from const.urls import Websites


class UrlScraper:
    def __init__(self, website: Websites, country: Countries):
        self.website = website
        self.country = country

    def scrape(self, url: str) -> List[Link]:
        raise NotImplementedError()
