from models.job import Job
from models.db_connection import db
from const.urls import Websites
from const.countries import Countries


with db.cursor() as cursor:
    cursor.execute("TRUNCATE TABLE job_posts")
    db.commit()


def test_constructor():
    job = Job(
        external_id="abc123",
        origin="indeed",
        title="Python Developer",
        company="Test Company",
        url="/job1",
        country="GB",
        salary="50K+",
        location="London",
        job_type="Permanent",
        description="This is the job description",
        active=True,
    )

    assert job.external_id == "abc123"
    assert job.origin == "indeed"
    assert job.title == "Python Developer"
    assert job.url == "/job1"
    assert job.country == "GB"
    assert job.salary == "50K+"
    assert job.location == "London"
    assert job.job_type == "Permanent"
    assert job.description == "This is the job description"
    assert job.active == True


def test_save():
    job = Job(
        external_id="abc123",
        origin="indeed",
        title="Python Developer",
        company="Test Company",
        url="/job1",
        country="GB",
        salary="50K+",
        location="London",
        job_type="Permanent",
        description="This is the job description",
        active=True,
    )

    id = job.save()

    result = Job.find_by_id(id)
    assert result.id == id
    assert result.origin == "indeed"
    assert result.title == "Python Developer"
    assert result.url == "/job1"
    assert result.country == "GB"
    assert result.salary == "50K+"
    assert result.location == "London"
    assert result.job_type == "Permanent"
    assert result.description == "This is the job description"
    assert result.active == True

def test_get_enums():
    country = Countries.GB
    website = Websites.INDEED

    job = Job(
        external_id="abc123",
        origin=website.value,
        title="Python Developer",
        company="Test Company",
        url="/job1",
        country=country.value,
        salary="50K+",
        location="London",
        job_type="Permanent",
        description="This is the job description",
        active=True,
    )
    assert country == job.getCountry()
    assert website == job.getWebsite()

    
