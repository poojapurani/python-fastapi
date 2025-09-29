from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

class ItemResponse(BaseModel):
    name: str
    price: float
    is_offer: bool = False

@app.post("/items/", response_model= ItemResponse)
def create_item(item: Item):
    print(item)
    return item
    