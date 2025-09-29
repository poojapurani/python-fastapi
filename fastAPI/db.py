# database.py
from sqlalchemy import create_engine, MetaData
from databases import Database   # <-- comes from 'databases' package


DATABASE_URL = "sqlite:///C:/Users/Lenovo/Desktop/Python course/fastAPI/users.db"


# Async database (used in routes)
database = Database(DATABASE_URL)

# SQLAlchemy engine + metadata
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = MetaData()
