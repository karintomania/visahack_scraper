import unittest
from unittest.mock import patch

from expiration_checker.indeed_expiration_checker import IndeedExpirationChecker


class TestIndeedExpirationChecker(unittest.TestCase):
    def setUp(self):
        self.checker = IndeedExpirationChecker()

    @patch("expiration_checker.indeed_expiration_checker.read_html")
    def test_is_url_expired_returns_true_on_expired_url(self, read_html_mock):
        read_html_mock.return_value = """<h1>Test Job</h1>
        <p>This job has expired on Indeed</p>"""

        result = self.checker.is_url_expired("http://expample.com/test_url")
        self.assertTrue(result)

    @patch("expiration_checker.indeed_expiration_checker.read_html")
    def test_is_url_expired_returns_false_on_valid_url(self, read_html_mock):
        read_html_mock.return_value = """<h1>Test Job</h1>
        <p>This job is still valid</p>"""
        result = self.checker.is_url_expired("http://expample.com/test_url")
        self.assertFalse(result)
