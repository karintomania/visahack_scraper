from typing import List
from models.job import Job
from models.link import Link
from scraper.read_html import read_html
from bs4 import BeautifulSoup
from const.countries import Countries, queries, link_prifixes

class IndeedUrlScraper:

    def scrape(self, country: str, page: int):

        start_index = page * 10
        url = queries[Countries.GB].format(start_index)
        
        html_source = read_html(url)

        result = self.get_list(html_source, country)

        return result

    def get_list(self, html: str, country: str) -> List[Link]:
        soup = BeautifulSoup(html, "html.parser")
        urls: List[Link] = []
        beacons = soup.find_all(class_="job_seen_beacon")

        for beacon in beacons:
            job_data = beacon.find("table")
            job_title = job_data.find("h2")
            uri = job_title.find("a").get("href")
            link = link_prifixes[Countries.GB].format(uri)
            external_id = job_title.find("a").get("data-jk")

            job_link = Link(external_id=external_id, origin="indeed", url=link, country=country)
            urls.append(job_link)

        return urls
