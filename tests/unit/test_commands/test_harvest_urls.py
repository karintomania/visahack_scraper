from commands.harvest_urls import harvest_urls
from unittest.mock import MagicMock, call, patch, create_autospec
from scraper.urls.indeed_url_scraper import IndeedGbUrlScraper
from const.countries import Countries
from const.urls import Websites


@patch("commands.harvest_urls.SLEEP_BETWEEN_URL", 0)
@patch("commands.harvest_urls.SCRAPING_RETRY_ON_ERROR", 3)
@patch("commands.harvest_urls.generate_url")
@patch("scraper.urls.indeed_url_scraper.IndeedGbUrlScraper")
def test_harvest_urls_retrys_with_errors_on_scrape(Scraper, generate_url_mock):
    generate_url_mock.return_value = ["http://example.com"]
    scraper = Scraper()
    scraper.website = Websites.INDEED
    scraper.country = Countries.GB

    scraper.scrape.side_effect = Exception("test exception")
    harvest_urls(scraper)

    scraper.scrape.assert_has_calls([call("http://example.com")] * 3)
