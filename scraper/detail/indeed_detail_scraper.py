import json
import re
from models.job import Job
from models.link import Link
from scraper.read_html import read_html


class IndeedDetailScraper:

    def scrape(self, link:Link):
        html_source = read_html(link.url)

        with open("test.html", "w") as ht:
            ht.write(html_source)

        result = self.get_detail(html_source)
        result.url = link.url
        result.country = link.country

        return result

    def get_detail(self, html: str):
        match_json = re.search("window._initialData=(.*?});\n", html)

        json_str = match_json.group(1)
        job_details_json = json.loads(str(json_str))

        title = job_details_json["jobTitle"]
        external_id = job_details_json['jobKey']
        location = job_details_json['jobLocation']

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
            salary=salary,
            location=location,
            job_type=job_type,
            description=description,
            active=True
        )

        return job
