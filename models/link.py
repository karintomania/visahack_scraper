from typing import List
from models.db_connection import db
from const.urls import Websites
from const.countries import Countries


class Link:

    def __init__(
        self,
        id=None,
        external_id: str = "",
        origin: str = "",
        url: str = "",
        country: str = "",
        has_detail: bool = False,
        created_at=None,
    ):
        self.id = id
        self.external_id = external_id
        self.origin = origin
        self.url = url
        self.country = country
        self.has_detail = has_detail
        self.created_at = created_at

    @classmethod
    def find_by_id(cls, id: int):
        query = "SELECT * FROM job_links WHERE id = %s"

        with db.cursor() as cursor:
            cursor.execute(query, (id,))
            record = cursor.fetchone()

        if record:
            link = cls(
                id=record[0],
                external_id=record[1],
                origin=record[2],
                url=record[3],
                country=record[4],
                has_detail=bool(record[5]),
                created_at=record[6],
            )

            return link

        return None

    @classmethod
    def find_no_details(cls, websites: Websites , country: Countries):
        query = """SELECT * FROM job_links
                WHERE has_detail = 0
                AND origin = %s
                AND country = %s
                AND created_at >= CURDATE() - INTERVAL 3 DAY"""

        with db.cursor() as cursor:
            cursor.execute(query, (websites.value, country.value))
            records = cursor.fetchall()

        links: List[Link] = []
        for record in records:
            link = cls(
                id=record[0],
                external_id=record[1],
                origin=record[2],
                url=record[3],
                country=record[4],
                has_detail=bool(record[5]),
                created_at=record[6],
            )
            links.append(link)

        return links

    def save(self) -> int:
        if self.id is None:
            return self._insert_record()
        else:
            return self._update_record()

    def _update_record(self) -> int:
        update_query = (
            "UPDATE job_links "
            "SET external_id = %s, origin = %s, url = %s, country = %s, has_detail = %s "
            "WHERE id = %s"
        )
        data = (
            self.external_id,
            self.origin,
            self.url,
            self.country,
            1 if self.has_detail else 0,
            self.id,
        )
        with db.cursor() as cursor:
            cursor.execute(update_query, data)
            db.commit()
        return self.id

    def _insert_record(self) -> int:
        insert_query = (
            "INSERT INTO job_links "
            "(external_id, origin, url, country, has_detail) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        data = (
            self.external_id,
            self.origin,
            self.url,
            self.country,
            1 if self.has_detail else 0,
        )
        with db.cursor() as cursor:
            cursor.execute(insert_query, data)
            id = cursor.lastrowid
            db.commit()
        return id

    def getCountry(self) -> Countries:
        return Countries(self.country)

    def getWebsite(self) -> Websites:
        return Websites(self.origin)
