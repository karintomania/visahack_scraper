from scraper.detail.indeed_detail_scraper import IndeedDetailScraper

class IndeedDetailScraperUs(IndeedDetailScraper):


    def get_detail(self, html: str, country: str):
        job_details_json = super().get_job_details_json(html)

        
        benefits = job_details_json["benefitsModel"]["benefits"]
        for benefit in benefits:
            print(benefit["label"])

        job = super().create_basic_job(job_details_json, country)

        
        return job
