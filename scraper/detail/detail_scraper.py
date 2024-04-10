from models.job import Job
from models.link import Link
from const.countries import Countries
from const.urls import Websites
import bleach

class DetailScraper:

    def __init__(self, website: Websites, country: Countries):
        self.country = country
        self.website = website

    def scrape(self, link: Link) -> Job:
        pass

    def sanitise_html(self, html: str) -> str:

        allowed_tags = [
            'a', 'abbr', 'b', 'blockquote', 'code', 'del', 'em', 'i', 
            'li', 'ol', 'ul', 'p', 'pre', 'span', 'strong', 'sub', 'sup', 
            'u', 'br', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
        ]

        allowed_attributes = {
            'a': ['href'],
        }

        clean_html = bleach.clean(html,
                                  tags=allowed_tags,
                                  attributes=allowed_attributes,
                                  strip=True)
        return clean_html
