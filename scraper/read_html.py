from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import re
import datetime
from scraper.option import get_options


def read_html(url: str) -> str:
    options = get_options()
    s = Service("/usr/bin/chromedriver")
    with webdriver.Chrome(service=s, options=options) as driver:
        driver.get(url)
        html_source = driver.page_source

    return html_source
