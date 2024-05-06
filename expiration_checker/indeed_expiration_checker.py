from const.countries import Countries
from const.urls import Websites
from expiration_checker.expiration_checker import ExpirationChecker
from scraper.read_html import read_html


class IndeedExpirationChecker(ExpirationChecker):
    def __init__(self, country: Countries):
        super().__init__(Websites.INDEED, country)

    def is_url_expired(self, url: str) -> bool:
        html_source = read_html(url)

        result = self.is_html_expired(html_source)

        return result

    def is_html_expired(self, html: str) -> bool:
        print(html[:400])
        keyword = "This job has expired on Indeed"

        return keyword in html


class IndeedGbExpirationChecker(IndeedExpirationChecker):
    def __init__(self):
        super().__init__(Countries.GB)
