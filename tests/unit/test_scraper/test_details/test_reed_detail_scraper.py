import unittest
from pathlib import Path
from unittest.mock import patch

import pytest
from pytest import raises

from const.countries import Countries
from models.job import Websites
from models.link import Link
from scraper.detail.detail_scraper import DetailScraper
from scraper.detail.reed_detail_scraper import ReedDetailScraper
from scraper.detail.no_sponsor_exception import NoSponsorException


class TestReedDetailScraper(unittest.TestCase):
    @patch("scraper.detail.reed_detail_scraper.read_html")
    def test_get_detail_gets_job_detail(self, read_html):
        scraper = ReedDetailScraper(Countries.GB)

        html_path = str(Path(__file__).parent) + "/reed_details.html"
        with open(html_path, "r") as html_file:
            html_source = html_file.read()

        read_html.return_value = html_source

        link = Link(
            1,
            "job12345",
            Websites.REED.value,
            "https://reed.example.com/job/12345",
            Countries.GB.value,
        )
        result = scraper.scrape(link)

        self.assertEqual("job12345", result.external_id)
        self.assertEqual("Software Developer", result.title)
        self.assertEqual("Test Company", result.company)
        self.assertEqual("Manchester, Lancashire", result.location)
        self.assertEqual("Permanent,full-time", result.job_type)
        self.assertEqual("£35,000 - £45,000 per annum", result.salary)
        self.assertEqual(
            """ <p>
  <strong>
   Software Developer
  </strong>
 </p>
 <p>
  This is a test description.
 </p>""",
            result.description,
        )
