from const.countries import Countries
from const.urls import Websites
from scraper.urls import url_generator


def test_generate_url_generates_urls():
    country = Countries.GB
    website = Websites.INDEED

    mock_target_links = {
        Websites.INDEED: {
            Countries.GB: {
                "queries": (
                    "https://test.example/?q=engineer&start={}",
                    "https://test.example/?q=developer&start={}",
                ),
                "pages_to_scrape": 2,
            },
        },
    }

    url_generator.target_links = mock_target_links
    urls = url_generator.generate_url(website, country)

    assert 4 == len(urls)

    assert "https://test.example/?q=engineer&start=0" == urls[0]
    assert "https://test.example/?q=engineer&start=1" == urls[1]
    assert "https://test.example/?q=developer&start=0" == urls[2]
    assert "https://test.example/?q=developer&start=1" == urls[3]
