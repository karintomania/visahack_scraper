from models.job import Job
from models.link import Link
from const.countries import Countries
from const.urls import Websites

class DetailScraper:

    def __init__(self, website: Websites, country: Countries):
        self.country = country
        self.website = website

    def scrape(self, link: Link) -> Job:
        pass
