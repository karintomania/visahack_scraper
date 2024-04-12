from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import re
import datetime
from scraper.option import get_options
import atexit


class WebDriver:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            options = get_options()
            s = Service("/usr/bin/chromedriver")
            cls._instance = webdriver.Chrome(service=s, options=options)
            atexit.register(cls._close_driver)
        return cls._instance

    @classmethod
    def _close_driver(cls):
        if cls._instance:
            cls._instance.quit()
            cls._instance = None


def read_html(url: str) -> str:
    driver = WebDriver.get_instance()
    driver.get(url)
    html_source = driver.page_source

    return html_source
