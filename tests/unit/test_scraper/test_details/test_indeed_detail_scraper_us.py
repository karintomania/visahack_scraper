from pathlib import Path
from scraper.detail.indeed_detail_scraper_us import IndeedDetailScraperUs
import pytest
from scraper.detail.no_sponsor_exception import NoSponsorException

ids = IndeedDetailScraperUs()


def test_get_detail_gets_job_detail():
    html_path = str(Path(__file__).parent) + "/indeed_details.html"
    with open(html_path, "r") as html_file:
        html_source = html_file.read()
    country = "US"

    result = ids.get_detail(html_source, country)

    assert result.external_id == "14ffe2be7ba7b921"
    assert result.title == "Full Stack Developer"
    assert result.company == "Example.co.uk"
    assert result.country == country
    assert result.location == "Remote"
    assert result.job_type == "Permanent, Full-time"
    assert result.salary == "From £55,000 a year"
    assert result.description == "test description"

def test_get_detail_raise_no_sponsorship_exception():
    html_path = str(Path(__file__).parent) + "/indeed_details_no_visa.html"
    with open(html_path, "r") as html_file:
        html_source = html_file.read()

    country = "US"

    with pytest.raises(NoSponsorException) as e:
        ids.get_detail(html_source, country)

    assert str(e.value) == "This job doesn't offer sponsorship"
