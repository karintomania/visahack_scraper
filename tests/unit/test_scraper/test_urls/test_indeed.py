from pathlib import Path
from scraper.urls.indeed_url_scraper import IndeedGbUrlScraper

gb_scraper = IndeedGbUrlScraper()


def test_get_list_gets_list_gb():

    test_html = str(Path(__file__).parent) + "/test_indeed.html"
    with open(test_html, "r") as file:
        html = file.read()

        result = scraper.get_list(html)
        assert result[0].url == "https://uk.indeed.com/job1"
        assert result[0].origin == "indeed"
        assert result[0].external_id == "abc01"
        assert result[0].country == "GB"
        assert result[1].url == "https://uk.indeed.com/job2"
        assert result[1].external_id == "abc02"
        assert result[1].origin == "indeed"
        assert result[1].country == "GB"


def test_get_list_gets_list_us():
    pass

    # test_html = str(Path(__file__).parent) + "/test_indeed.html"
    # with open(test_html, "r") as file:
    #     html = file.read()

    #     result = scraper.get_list(html)
    #     assert result[0].url == "https://uk.indeed.com/job1"
    #     assert result[0].origin == "indeed"
    #     assert result[0].external_id == "abc01"
    #     assert result[0].country == "GB"
    #     assert result[1].url == "https://uk.indeed.com/job2"
    #     assert result[1].external_id == "abc02"
    #     assert result[1].origin == "indeed"
    #     assert result[1].country == "GB"
