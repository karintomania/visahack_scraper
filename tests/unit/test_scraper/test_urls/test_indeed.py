from pathlib import Path
from scraper.urls.indeed_url_scraper import IndeedGbUrlScraper, IndeedUsUrlScraper
import unittest
from unittest.mock import patch
import pytest


@patch("scraper.urls.indeed_url_scraper.read_html")
def test_get_list_gets_list_gb(read_mock):
    scraper = IndeedGbUrlScraper()
    test_html = str(Path(__file__).parent) + "/test_indeed.html"

    with open(test_html, "r") as file:
        html = file.read()

        read_mock.return_value = html

        # result = scraper.get_list(html)
        result = scraper.scrape("test.example")
        assert result[0].url == "https://uk.indeed.com/job1"
        assert result[0].origin == scraper.website.value
        assert result[0].external_id == "abc01"
        assert result[0].country == scraper.country.value
        assert result[1].url == "https://uk.indeed.com/job2"
        assert result[1].external_id == "abc02"
        assert result[1].origin == scraper.website.value
        assert result[1].country == scraper.country.value


# TODO: write test for US
