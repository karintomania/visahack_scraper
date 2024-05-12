from unittest.mock import patch
from commands.harvest_urls import harvest_urls
from scraper.urls.indeed_url_scraper import IndeedGbUrlScraper


scraper = IndeedGbUrlScraper()

with patch("commands.harvest_urls.generate_url") as mock_generate:
    mock_generate.return_value = [
        "https://uk.indeed.com/jobs?q=software+engineer+%22UK+visa+sponsorship%22&l=United+Kingdom&sort=date&start=0"
    ]
    harvest_urls(scraper)
