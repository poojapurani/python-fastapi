from sqlalchemy import Column,Integer, String, Float
from db2 import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer,primary_key=True,index=True)
    name = Column( String(50),unique=True, nullable=False,index= True )
    price = Column(Float,nullable=False)
    quantity = Column(Integer,default=00)