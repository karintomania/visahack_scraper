from const.countries import Countries
from enum import Enum

class Websites(Enum):
    INDEED = "indeed"
    REED = "reed"


queries = {
    Websites.INDEED:{
        Countries.GB: "https://uk.indeed.com/jobs?q=software+engineer+%22UK+visa+sponsorship%22&l=United+Kingdom&sort=date&start={}",
        Countries.US: "https://www.indeed.com/jobs?q=software+engineer+%22Visa+sponsorship%22&l=United+States&sort=date&start={}",
    },
}
link_prefixes = {
    Websites.INDEED:{
        Countries.GB: "https://uk.indeed.com{}",
        Countries.US: "https://indeed.com{}",
    },
}
