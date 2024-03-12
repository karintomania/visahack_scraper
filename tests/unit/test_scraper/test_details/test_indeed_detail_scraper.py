from pathlib import Path
from scraper.detail.indeed_detail_scraper import IndeedDetailScraper

ids = IndeedDetailScraper()


def test_get_detail_gets_job_detail():
    html_path = str(Path(__file__).parent) + "/indeed_details.html"
    with open(html_path, "r") as html_file:
        html_source = html_file.read()

        result = ids.get_detail(html_source)

    assert result.external_id == "14ffe2be7ba7b921"
    assert result.title == "Full Stack Developer"
    assert result.company == "Example.co.uk"
    assert result.location == "Remote"
    assert result.job_type == "Permanent, Full-time"
    assert result.salary == "From £55,000 a year"
    assert result.description[:17] == "<p><b>Salary:</b>"
