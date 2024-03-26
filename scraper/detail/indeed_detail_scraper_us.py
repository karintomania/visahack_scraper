from scraper.detail.indeed_detail_scraper import IndeedDetailScraper
from scraper.detail.no_sponsor_exception import NoSponsorException


class IndeedDetailScraperUs(IndeedDetailScraper):

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
