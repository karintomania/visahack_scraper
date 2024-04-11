from scraper.detail.detail_scraper import DetailScraper
from const.countries import Countries
from const.urls import Websites


def test_sanitise_html_remove_tags_and_attrs():

    ds = DetailScraper(Websites.INDEED, Countries.GB)
    html = """<h1 onclick="malicious()">Test Header</h1>
    <script>some js;</script>
    <p>Safe <strong>content</strong> with a <a href="http://example.com" onclick="stealCookies()">link</a></p>
    <img src="https://example.com/image.png" onerror="javascript:alert('XSS attempt')" />"""

    cleaned = ds.sanitise_html(html)

    expected = """<h1>Test Header</h1>
    some js;
    <p>Safe <strong>content</strong> with a <a href="http://example.com">link</a></p>
    """
    assert expected == cleaned
