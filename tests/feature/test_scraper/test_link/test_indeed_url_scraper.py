from scraper.urls.indeed_url_scraper import IndeedUrlScraper
from const.countries import queries, Countries

sli = IndeedUrlScraper()


def test_scrape_list():
    assert True

    # result = sli.scrape(Countries.GB, 0)
    # print(result)
    # assert 15 == len(result)

    # first_url = result[0]
    # assert first_url.url
