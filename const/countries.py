from enum import Enum


class Countries(Enum):
    GB = "GB"
    US = "US"
    AU = "AU"


queries = {
    Countries.GB: "https://uk.indeed.com/jobs?q=software+engineer+%22UK+visa+sponsorship%22&l=United+Kingdom&sort=date&start={}"
}
link_prefixes = {Countries.GB: "https://uk.indeed.com{}"}
