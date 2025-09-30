from sqlalchemy import Column, Table, Integer, String
from db import metadata
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("username", String(50), unique=True, nullable=False, index=True),
    Column("password", String, nullable=False)
)
