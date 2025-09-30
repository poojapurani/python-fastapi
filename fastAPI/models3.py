from database2 import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"   # <-- double underscores

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
