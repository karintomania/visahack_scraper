import json
import re
from models.job import Job
from models.link import Link
from scraper.read_html import read_html
from const.countries import Countries
from scraper.detail.detail_scraper import DetailScraper


class IndeedDetailScraper(DetailScraper):

    def __init__(self):
        self.country = Countries.GB

    def scrape(self, link: Link) -> Job:
        html_source = read_html(link.url)

        with open("test.html", "w") as ht:
            ht.write(html_source)

        result = self.get_detail(html_source, link.country)
        result.url = link.url

        return result

    def get_detail(self, html: str, country: str) -> Job:
        job_details_json = self.get_job_details_json(html)

        job = self.create_basic_job(job_details_json, country)
        return job

    def create_basic_job(self, job_details_json, country) -> Job:
        title = job_details_json["jobTitle"]
        benefits = job_details_json["benefitsModel"]["benefits"]
        external_id = job_details_json["jobKey"]
        location = job_details_json["jobLocation"]

        job_info_model = job_details_json["jobInfoWrapperModel"]["jobInfoModel"]
        company = job_info_model["jobInfoHeaderModel"]["companyName"]
        # location = job_info_model["jobInfoHeaderModel"]["formattedLocation"]
        description = job_info_model["sanitizedJobDescription"]
        job_type = job_info_model["jobMetadataHeaderModel"]["jobType"]

        salary_info_model = job_details_json["salaryInfoModel"]
        if salary_info_model:
            salary = salary_info_model["salaryText"]
        else:
            salary = None

        job = Job(
            external_id=external_id,
            origin="indeed",
            title=title,
            company=company,
            country=country,
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
    pass



class IndeedUsDetailScraper(IndeedDetailScraper):

    def get_detail(self, html: str, country: str):
        job_details_json = super().get_job_details_json(html)

        benefits = job_details_json["benefitsModel"]["benefits"]

        if not self.has_sponsorship(benefits):
            raise NoSponsorException("This job doesn't offer sponsorship")

        job = super().create_basic_job(job_details_json, country)

        return job

    def has_sponsorship(self, benefits) -> bool:

        sponsorship = any(
            benefit["label"] == "Visa Sponsorship" for benefit in benefits
        )
        return sponsorship
