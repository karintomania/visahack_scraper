from scraper.urls.indeed_url_scraper import IndeedUrlScraper

sli = IndeedUrlScraper()


def test_scrape_list():
    result = sli.scrape_list()
    print(result)
    assert 15 == len(result)

    first_job = result[0]
    assert first_job.get("title")
    assert first_job.get("link")
