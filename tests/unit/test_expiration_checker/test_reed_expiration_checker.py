import unittest
from unittest.mock import patch

from expiration_checker.reed_expiration_checker import ReedExpirationChecker


class TestReedExpirationChecker(unittest.TestCase):
    def setUp(self):
        self.checker = ReedExpirationChecker()

    @patch("expiration_checker.reed_expiration_checker.read_html")
    def test_is_url_expired_returns_true_on_expired_url(self, read_html_mock):
        read_html_mock.return_value = """<h1>Test Job</h1>
        <p>The following job is no longer available: Software Engineer</p>"""

        result = self.checker.is_url_expired("http://expample.com/test_url")
        self.assertTrue(result)

    @patch("expiration_checker.reed_expiration_checker.read_html")
    def test_is_url_expired_returns_false_on_valid_url(self, read_html_mock):
        read_html_mock.return_value = """<h1>Test Job</h1>
        <p>This job is still valid</p>"""
        result = self.checker.is_url_expired("http://expample.com/test_url")
        self.assertFalse(result)
