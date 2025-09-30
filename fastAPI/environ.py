from fastapi import FastAPI
from conf import settings

app = FastAPI()

print(settings.database_url)

@app.get("/")
async def root():
    return {"db_url":settings.database_url,"secret_key": settings.secret_key}