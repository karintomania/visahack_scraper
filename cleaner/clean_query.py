from models.db_connection import db
from const.common import JOB_EXPIRED_DAYS, JOB_REMOVAL_DAYS, LINK_REMOVAL_DAYS


def deactivate_jobs():
    with db.cursor() as cursor:

        deactivate_query = f"""
        UPDATE job_posts
        SET active = 0
        WHERE created_at < DATE_SUB(NOW(), INTERVAL {JOB_EXPIRED_DAYS} DAY);
        """
        cursor.execute(deactivate_query)

        db.commit()
        return cursor.rowcount


def clean_jobs():
    with db.cursor() as cursor:

        delete_query = f"""
        DELETE FROM job_posts 
        WHERE created_at < DATE_SUB(NOW(), INTERVAL {JOB_REMOVAL_DAYS} DAY);
        """
        cursor.execute(delete_query)

        db.commit()
        return cursor.rowcount


def clean_links():
    with db.cursor() as cursor:

        delete_query = f"""
        DELETE FROM job_links 
        WHERE created_at < DATE_SUB(NOW(), INTERVAL {LINK_REMOVAL_DAYS} DAY);
        """
        cursor.execute(delete_query)

        db.commit()
        return cursor.rowcount
