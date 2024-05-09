import unittest

from const.countries import Countries
from const.urls import Websites
from models.db_connection import db
from models.job import Job
from datetime import datetime, timedelta


class JobTestCase(unittest.TestCase):
    def setUp(self):
        with db.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE job_posts")
            db.commit()

    def test_constructor(self):
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

    def test_save(self):
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

    def test_get_enums(self):
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

    def test_get_expiration_check_target_returns_target_jobs(self):
        new_job = Job(
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
        old_job = Job(
            external_id="abc124",
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
        old_job_id = old_job.save()
        new_job_id = new_job.save()

        old_date = datetime.now() - timedelta(days=10)
        old_date_str = old_date.strftime("%Y-%m-%d, %H:%M:%S")

        with db.cursor() as cursor:
            cursor.execute(
                """
                UPDATE job_posts SET updated_at = %s
                WHERE id = %s
            """,
                (old_date_str, old_job_id),
            )

        result = Job.get_expiration_check_target(Websites.INDEED)

        self.assertEqual(1, len(result))
        self.assertEqual(old_job_id, result[0].id)

        pass
