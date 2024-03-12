from scraper.details.indeed_detail_scraper import IndeedDetailScraper

sdi = IndeedDetailScraper()


def test_scrape_list():
    result = sdi.scrape_list()
    # print(result)
    # assert 15 == len(result)

    # first_job = result[0]
    # assert first_job.get('title')
    # assert first_job.get('link')
