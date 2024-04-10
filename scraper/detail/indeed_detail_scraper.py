import json
import re
from models.job import Job
from models.link import Link
from scraper.read_html import read_html
from const.countries import Countries
from const.urls import Websites
from scraper.detail.detail_scraper import DetailScraper
from scraper.detail.no_sponsor_exception import NoSponsorException


class IndeedDetailScraper(DetailScraper):

    def __init__(self, country: Countries = Countries.GB):
        super().__init__(Websites.INDEED, country)

    def scrape(self, link: Link) -> Job:
        html_source = read_html(link.url)

        job = self.get_detail(html_source)
        job.url = link.url

        return job

    def get_detail(self, html: str) -> Job:
        job_details_json = self.get_job_details_json(html)

        if not self.validate_sponsorship(job_details_json):
            raise NoSponsorException("This job doesn't offer sponsorship")

        job = self.harvest_details(job_details_json)
        return job

    def validate_sponsorship(self, job_details_json) -> bool:

        if not job_details_json["benefitsModel"]: # Jobs doesn't display benefits
            return False

        benefits = job_details_json["benefitsModel"]["benefits"]

        # check if one of the benefits includes "Visa Sponsorship"
        has_sponsorship = any(
            "visa sponsorship" in benefit["label"].lower() for benefit in benefits
        )

        return has_sponsorship 

    def harvest_details(self, job_details_json) -> Job:
        title = job_details_json["jobTitle"]
        benefits = job_details_json["benefitsModel"]["benefits"]
        external_id = job_details_json["jobKey"]
        location = job_details_json["jobLocation"]

        job_info_model = job_details_json["jobInfoWrapperModel"]["jobInfoModel"]
        company = job_info_model["jobInfoHeaderModel"]["companyName"]
        description = self.sanitise_html(job_info_model["sanitizedJobDescription"])
        job_type = job_info_model["jobMetadataHeaderModel"]["jobType"]

        salary_info_model = job_details_json["salaryInfoModel"]
        if salary_info_model:
            salary = salary_info_model["salaryText"]
        else:
            salary = None

        job = Job(
            external_id=external_id,
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

    def get_job_details_json(self, html):
        match_json = re.search("window._initialData=(.*?});\n", html)

        json_str = match_json.group(1)
        job_details_json = json.loads(str(json_str))
        return job_details_json

class IndeedGbDetailScraper(IndeedDetailScraper):
    def __init__(self):
        super().__init__(Countries.GB)
    pass



class IndeedUsDetailScraper(IndeedDetailScraper):
    def __init__(self):
        super().__init__(Countries.US)
    pass

