# from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.engine import URL

# from sqlalchemy.orm import declarative_base, sessionmaker
#
db_url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="password",
    host="localhost",
    database="demo-repo",
    port=5432,
)
