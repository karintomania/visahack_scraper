from models.job import Job
from models.link import Link
from models.db_connection import db
from datetime import datetime, timedelta
from const.common import JOB_EXPIRED_DAYS, JOB_REMOVAL_DAYS
from cleaner.clean_query import deactivate_jobs, clean_links


target_job_id: int = 1
target_link_id: int = 1


def insert_job(cursor, job_expired):
    # insert a expired job
    query = (
        "INSERT INTO jobs "
        "(external_id, origin, title, company, url, country, salary, location, job_type, description, active, created_at) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    )
    data = (
        "ext_123",
        "indeed",
        "Senior Developer",
        "Acme",
        "http://exmample.com",
        "GB",
        "50K",
        "London",
        "Full time",
        "Description of the company",
        1,
        job_expired.strftime("%Y-%m-%d %H:%M:%S"),
    )

    cursor.execute(query, data)

    return cursor.lastrowid


def insert_link(cursor, link_expired):
    query = (
        "INSERT INTO job_links "
        "(external_id, origin, url, country, has_detail, created_at) "
        "VALUES (%s, %s, %s, %s, %s, %s)"
    )
    data = (
        "ext_123",
        "indeed",
        "http://exmample.com",
        "GB",
        1,
        link_expired.strftime("%Y-%m-%d %H:%M:%S"),
    )

    cursor.execute(query, data)

    target_job_id = cursor.lastrowid
    return target_job_id


with db.cursor() as cursor:
    cursor.execute("TRUNCATE TABLE jobs")
    cursor.execute("TRUNCATE TABLE job_links")

    now = datetime.now()

    job_expired = now - timedelta(days=(JOB_EXPIRED_DAYS + 1))
    link_expired = now - timedelta(days=(JOB_REMOVAL_DAYS + 1))

    # insert a expired job
    target_job_id = insert_job(cursor, job_expired)

    target_link_id = insert_link(cursor, link_expired)

    db.commit()


def test_deactivate_jobs():
    job = Job.find_by_id(target_job_id)

    # the job is active when it's created
    assert job.active == True

    row_count = deactivate_jobs()

    updated_job = Job.find_by_id(target_job_id)
    assert updated_job.active == False
    assert row_count == 1


def test_clean_links():
    link = Link.find_by_id(target_link_id)

    # the link is active when it's created
    assert link.id == target_link_id

    row_count = clean_links()

    updated_link = link.find_by_id(target_link_id)
    assert updated_link == None
    assert row_count == 1
