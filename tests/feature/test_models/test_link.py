from models.link import Link
from models.db_connection import db

with db.cursor() as cursor:
    cursor.execute("TRUNCATE TABLE job_links")
    db.commit()


def test_constructor():
    l = Link(
        external_id="abc123",
        origin="indeed",
        url="/job1",
        country="GB",
    )

    assert l.external_id == "abc123"
    assert l.origin == "indeed"
    assert l.url == "/job1"
    assert l.country == "GB"


def test_save():
    l = Link(
        external_id="abc123",
        origin="indeed",
        url="/job1",
        country="GB",
    )

    id = l.save()

    result = Link.find_by_id(1)
    assert result.id == 1
    assert result.external_id == "abc123"
    assert result.origin == "indeed"
    assert result.url == "/job1"
    assert result.country == "GB"
