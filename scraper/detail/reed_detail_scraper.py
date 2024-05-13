import json
import re
from models.job import Job
from models.link import Link
from scraper.read_html import read_html
from const.countries import Countries
from const.urls import Websites
from scraper.detail.detail_scraper import DetailScraper
from scraper.detail.no_sponsor_exception import NoSponsorException
from bs4 import BeautifulSoup


class ReedDetailScraper(DetailScraper):
    def __init__(self, country: Countries = Countries.GB):
        super().__init__(Websites.REED, country)

    def scrape(self, link: Link) -> Job:
        html_source = read_html(link.url)

        job = self.get_detail(link, html_source)
        job.url = link.url

        return job

    def get_detail(self, link: Link, html: str) -> Job:
        soup = BeautifulSoup(html, "html.parser")

        article = soup.select('article[class*="job row"]')[0]
        # article = soup.find("article")

        title = article.find("h1").text
        company = article.find(
            "span", attrs={"data-element": "about_recruiter"}
        ).text.strip()

        salary_span = article.find("span", attrs={"itemprop": "baseSalary"})
        salary = salary_span.text.strip() if salary_span else ""

        country_div = article.find("span", attrs={"id": "jobCountry"})
        if country_div:
            location_div = country_div.findNext("span")
            location = location_div.text.replace("\n", "").strip()
        else:
            location = ""

        job_type_span = article.find("span", attrs={"itemprop": "employmentType"})
        job_type = job_type_span.get_text(strip=True) if job_type_span else ""

        desc_span = article.find("span", attrs={"itemprop": "description"})
        desc_sanitised = self.sanitise_html(desc_span.prettify())

        # remove parent span tag
        desc_without_parent = desc_sanitised.splitlines()[1:-1]
        description = "\n".join(desc_without_parent)

        job = Job(
            external_id=link.external_id,
            origin=self.website.value,
            title=title,
            company=company,
            country=self.country.value,
            salary=salary,
            location=location,
            job_type=job_type,
            description=description,
            active=True,
        )

        return job

    def validate_sponsorship(self, html: str) -> bool:
        # in Reed, there is no indication of visa sponsorship in the HTML
        has_sponsorship = True
        return has_sponsorship


class ReedGbDetailScraper(ReedDetailScraper):
    def __init__(self):
        super().__init__(Countries.GB)

    pass


class ReedUsDetailScraper(ReedDetailScraper):
    def __init__(self):
        super().__init__(Countries.US)

    pass
