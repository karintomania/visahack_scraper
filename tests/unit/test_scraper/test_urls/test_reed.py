from pathlib import Path
from const.countries import Countries
from const.urls import Websites
from scraper.urls.reed_url_scraper import ReedGbUrlScraper
import unittest
from unittest.mock import patch
import pytest


class TestReedUrlScraper(unittest.TestCase):
    @patch("scraper.urls.reed_url_scraper.read_html")
    def test_get_list_gets_url_list(self, read_mock):
        scraper = ReedGbUrlScraper()

        test_html = str(Path(__file__).parent) + "/test_reed.html"

        with open(test_html, "r") as file:
            html = file.read()

            read_mock.return_value = html

            result = scraper.scrape("test.example")

            self.assertEqual("https://www.reed.co.uk/jobs/software-engineer/51867796", result[0].url)
            self.assertEqual(Websites.REED.value, result[0].origin)
            self.assertEqual("job51867796", result[0].external_id)
            self.assertEqual(Countries.GB.value, result[0].country)
            self.assertEqual("https://www.reed.co.uk/jobs/senior-software-engineer-sre/52507304", result[1].url)
            self.assertEqual(Websites.REED.value, result[1].origin)
            self.assertEqual("job52507304", result[1].external_id)
            self.assertEqual(Countries.GB.value, result[1].country)
