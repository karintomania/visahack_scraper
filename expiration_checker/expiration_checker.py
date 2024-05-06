from const.countries import Countries
from const.urls import Websites


class ExpirationChecker:
    def __init__(self, website: Websites, country: Countries):
        self.website = website
        self.country = country

    def is_url_expired(self, url: str) -> bool:
        raise NotImplementedError()

    def is_html_expired(self, html: str) -> bool:
        raise NotImplementedError()
