from models.link import Link
from models.db_connection import db
from const.urls import Websites
from const.countries import Countries

def reset_job_links_table():
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

def test_get_enums():
    country = Countries.GB
    website = Websites.INDEED
    l = Link(
        external_id="abc123",
        origin=website.value,
        url="/job1",
        country=country.value,
    )

    assert country == l.getCountry()
    assert website == l.getWebsite()

    


def test_save():
    reset_job_links_table()
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

    
def test_find_no_details():
    reset_job_links_table()
    links = (
        Link( # This should be selected
            external_id="abc001",
            origin=Websites.INDEED.value,
            url="/job1",
            country=Countries.GB.value,
            has_detail=False,
        ),
        Link(
            external_id="abc002",
            origin=Websites.INDEED.value,
            url="/job1",
            country=Countries.GB.value,
            has_detail=True, # Has details
        ),
        Link(
            external_id="abc003",
            origin=Websites.INDEED.value,
            url="/job1",
            country=Countries.US.value, # wrong country
            has_detail=False,
        ),
        Link(
            external_id="abc004",
            origin=Websites.REED.value, # wrong origin
            url="/job1",
            country=Countries.US.value,
            has_detail=False,
        ),
    )

    ids = [l.save() for l in links]

    result = Link.find_no_details(Websites.INDEED, Countries.GB)
    assert len(result) == 1
    assert ids[0] == result[0].id
