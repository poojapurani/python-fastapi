from urllib.parse import quote
from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional, List
from fastapi import FastAPI
from contextlib import asynccontextmanager

# Encode password
password = "Pto@3404"
encoded_password = quote(password)
postgres_uri = f"postgresql://postgres:{encoded_password}@db.ehdiwptwymjddtnxsyxx.supabase.co:5432/postgres"

# Model
class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    is_offer: bool = Field(default=False)

    class Config:
        orm_mode = True

# Engine
engine = create_engine(postgres_uri, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

# Routes
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

@app.get("/items/", response_model=List[Item])
def read_items():
    with Session(engine) as session:
        items = session.exec(select(Item)).all()
        return items
