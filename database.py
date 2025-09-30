from sqlmodel import create_engine, Session, SQLModel
from urllib.parse import quote
from db import DATABASE_URL

password = "Pto@3404"
encoded_password = quote(password)
postgres_uri = f"postgresql://postgres:{encoded_password}@db.ehdiwptwymjddtnxsyxx.supabase.co:5432/postgres"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = Session(autocommit=False, autoflush=False, bind=engine)

metadata = MetaData()
database = engine
