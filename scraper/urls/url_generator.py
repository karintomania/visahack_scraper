from typing import List
from const.countries import Countries
from const.urls import Websites

target_links = {
    Websites.INDEED: {
        Countries.GB: {
            "queries": (
                "https://uk.indeed.com/jobs?q=software+engineer+%22UK+visa+sponsorship%22&l=United+Kingdom&sort=date&start={}",
                "https://uk.indeed.com/jobs?q=developer+%22UK+visa+sponsorship%22&l=United+Kingdom&sort=date&start={}",
            ),
            "pages_to_scrape": 2,
        },
        Countries.US: {
            "queries": (
                "https://www.indeed.com/jobs?q=software+engineer+%22Visa+sponsorship%22&l=United+States&sort=date&start={}",
                "https://www.indeed.com/jobs?q=developer+%22Visa+sponsorship%22&l=United+States&sort=date&start={}",
            ),
            "pages_to_scrape": 3,
        },
    },
    Websites.REED: {
        Countries.GB: {
            "queries": (
                "https://www.reed.co.uk/jobs/software-engineer-jobs-in-united-kingdom?visaSponsorship=true?pageno={}",
                "https://www.reed.co.uk/jobs/software-developer-jobs-in-united-kingdom?visaSponsorship=true?pageno={}",
            ),
            "pages_to_scrape": 2,
        },
    },
}


def generate_url(website: Websites, country: Countries) -> List[str]:
    target = target_links[website][country]

    queries = target["queries"]
    page = target["pages_to_scrape"]

    urls = []
    for query in queries:
        for i in range(page):
            urls.append(query.format(str(i)))

    return urls
