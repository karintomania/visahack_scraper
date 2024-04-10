from pathlib import Path
from scraper.detail.indeed_detail_scraper import IndeedDetailScraper, IndeedGbDetailScraper, IndeedUsDetailScraper
from scraper.detail.detail_scraper import DetailScraper
from scraper.detail.no_sponsor_exception import NoSponsorException
from pytest import raises
import pytest
from const.countries import Countries

testdata = [
    (IndeedGbDetailScraper(), Countries.GB),
    (IndeedUsDetailScraper(), Countries.US),
]

@pytest.mark.parametrize("scraper, country", testdata)
def test_get_detail_gets_job_detail(scraper: DetailScraper, country: Countries):
    html_path = str(Path(__file__).parent) + "/indeed_details.html"
    with open(html_path, "r") as html_file:
        html_source = html_file.read()

        result = scraper.get_detail(html_source)

    assert result.external_id == "14ffe2be7ba7b921"
    assert result.title == "Full Stack Developer"
    assert result.company == "Example.co.uk"
    assert result.country == country.value
    assert result.location == "Remote"
    assert result.job_type == "Permanent, Full-time"
    assert result.salary == "From £55,000 a year"
    assert result.description == "<p>test description</p>"

@pytest.mark.parametrize("scraper, country", testdata)
def test_get_detail_throws_no_sponsor_exception(scraper: DetailScraper, country: Countries):
    html_path = str(Path(__file__).parent) + "/indeed_details_no_visa.html"
    with open(html_path, "r") as html_file:
        html_source = html_file.read()


    with raises(NoSponsorException):
        scraper.get_detail(html_source)

