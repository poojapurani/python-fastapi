from email.policy import HTTP
from fastapi import FastAPI,HTTPException

app = FastAPI()

@app.get("/divide")
def divide(a: float,b: float):
    if b==0:
        raise HTTPException(status_code=400,detail="Division by zero is not allowed")
    return {"result": a/b}

class NotFoundException(Exception):
    def __init__(self, name: str) :
        self.name = name

from fastapi.responses import JSONResponse
from fastapi.requests import Request  

@app.exception_handler(NotFoundException)