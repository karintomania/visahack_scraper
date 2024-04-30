from models.job import Job
from models.link import Link


def has_duplication(external_id: str) -> bool:
    job = Job.find_by_external_id(external_id)
    link = Link.find_by_external_id(external_id)

    job_exists = (job is not None) or (link is not None)
    return job_exists
