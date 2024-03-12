from selenium import webdriver
import re
import datetime
from scraper.option import get_options


def read_html(url: str) -> str:
    options = get_options()
    with webdriver.Chrome(options=options) as driver:
        driver.get(url)
        html_source = driver.page_source

    return html_source
