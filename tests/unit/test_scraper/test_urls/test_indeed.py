from pathlib import Path
from scraper.urls.indeed_url_scraper import IndeedUrlScraper

sli = IndeedUrlScraper()


def test_pytest():
    # sli.scrape_list()
    assert True


def test_get_list_gets_list():

    test_html = str(Path(__file__).parent) + "/test_indeed.html"
    with open(test_html, "r") as file:
        html = file.read()

        result = sli.get_list(html, "GB")
        assert result[0].url == "https://uk.indeed.com/job1"
        assert result[0].origin == "indeed"
        assert result[0].external_id == "abc01"
        assert result[0].country == "GB"
        assert result[1].url == "https://uk.indeed.com/job2"
        assert result[1].external_id == "abc02"
        assert result[1].origin == "indeed"
        assert result[1].country == "GB"
