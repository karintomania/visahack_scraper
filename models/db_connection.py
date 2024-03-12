import mysql.connector
from const.db import const_db

db = mysql.connector.connect(
    host=const_db["host"],
    port=const_db["port"],
    user=const_db["user"],
    password=const_db["password"],
    database=const_db["database"],
)
