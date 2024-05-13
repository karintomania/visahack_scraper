from datetime import datetime
from typing import List, Optional

from typing_extensions import Self

from const.common import EXPIRATION_CHECK_FREQUENCY_DAYS
from const.countries import Countries
from const.urls import Websites
from models.db_connection import db


class Job:
    def __init__(
        self,
        id=None,
        external_id: str = "",
        origin: str = "",
        title: str = "",
        company: str = "",
        url: str = "",
        country: str = "",
        salary: str = "",
        location: str = "",
        job_type: str = "",
        description: str = "",
        active: bool = False,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.id = id
        self.external_id = external_id
        self.origin = origin
        self.title = title
        self.company = company
        self.url = url
        self.country = country
        self.salary = salary
        self.location = location
        self.job_type = job_type
        self.description = description
        self.active = active
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def find_by_id(cls, id: int) -> Optional[Self]:
        query = "SELECT * FROM job_posts WHERE id = %s"
        with db.cursor() as cursor:
            cursor.execute(query, (id,))
            record = cursor.fetchone()
        if record:
            job = cls.convert_db_row(record)
            return job
        return None

    @classmethod
    def find_by_external_id(cls, id: int) -> Optional[Self]:
        query = "SELECT * FROM job_posts WHERE external_id = %s"
        with db.cursor() as cursor:
            cursor.execute(query, (id,))
            record = cursor.fetchone()
        if record:
            job = cls.convert_db_row(record)
            return job
        return None

    @classmethod
    def get_expiration_check_target(cls, website: Websites) -> List[Self]:
        query = """
        SELECT * FROM job_posts 
        WHERE updated_at < DATE_SUB(NOW(), INTERVAL %s DAY)
        AND active = 1
        AND origin = %s
        """

        with db.cursor() as cursor:
            cursor.execute(query, (EXPIRATION_CHECK_FREQUENCY_DAYS, website.value))
            records = cursor.fetchall()

        result = []
        for record in records:
            result.append(cls.convert_db_row(record))

        return result

    @classmethod
    def convert_db_row(cls, row) -> Self:
        job = cls(
            id=row[0],
            external_id=row[1],
            origin=row[2],
            title=row[3],
            company=row[4],
            url=row[5],
            country=row[6],
            salary=row[7],
            location=row[8],
            job_type=row[9],
            description=row[10],
            active=bool(row[11]),
            created_at=row[12],
            updated_at=row[13],
        )
        return job

    def save(self) -> int:
        if self.id is None:
            query, data = self.insert_row()

        else:
            query, data = self.update_row()

        with db.cursor() as cursor:
            cursor.execute(query, data)
            if self.id is None:
                self.id = (
                    cursor.lastrowid
                )  # This is only relevant for insert operations
            db.commit()

        return self.id

    def update_row(self):
        query = (
            "UPDATE job_posts SET "
            "external_id = %s, origin = %s, title = %s, company = %s, "
            "url = %s, country = %s, salary = %s, location = %s, "
            "job_type = %s, description = %s, active = %s, "
            "updated_at = CURRENT_TIMESTAMP "
            "WHERE id = %s"
        )
        data = (
            self.external_id,
            self.origin,
            self.title,
            self.company,
            self.url,
            self.country,
            self.salary,
            self.location,
            self.job_type,
            self.description,
            1 if self.active else 0,
            self.id,  # `id` is now part of data for the WHERE clause
        )
        return query, data

    def insert_row(self):
        query = (
            "INSERT INTO job_posts "
            "(external_id, origin, title, company, url, country, salary, location, job_type, description, active, created_at, updated_at) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
        )
        data = (
            self.external_id,
            self.origin,
            self.title,
            self.company,
            self.url,
            self.country,
            self.salary,
            self.location,
            self.job_type,
            self.description,
            1 if self.active else 0,
        )

        return query, data

    def getCountry(self) -> Countries:
        return Countries(self.country)

    def getWebsite(self) -> Websites:
        return Websites(self.origin)
