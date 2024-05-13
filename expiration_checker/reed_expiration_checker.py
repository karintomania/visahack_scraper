from const.countries import Countries
from const.urls import Websites
from expiration_checker.expiration_checker import ExpirationChecker
from scraper.read_html import read_html


class ReedExpirationChecker(ExpirationChecker):
    def __init__(self):
        # Reed doesn't have any difference between country. GB is just a placeholder.
        super().__init__(Websites.REED, Countries.GB)

    def is_url_expired(self, url: str) -> bool:
        html_source = read_html(url)

        result = self.is_html_expired(html_source)

        return result

    def is_html_expired(self, html: str) -> bool:
        keyword = "The following job is no longer available:"

        return keyword in html
