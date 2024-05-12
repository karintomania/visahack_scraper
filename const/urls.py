from const.countries import Countries
from enum import Enum


class Websites(Enum):
    INDEED = "indeed"
    REED = "reed"


link_prefixes = {
    Websites.INDEED: {
        Countries.GB: "https://uk.indeed.com{}",
        Countries.US: "https://indeed.com{}",
    },
    Websites.REED: {
        Countries.GB: "https://www.reed.co.uk{}",
        Countries.US: "https://www.reed.co.uk{}",
    },
}
