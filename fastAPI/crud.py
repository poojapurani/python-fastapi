from fastapi import FastAPI
from pydantic import BaseModel
from db2 import engine,SessionLocal
from models2 import Base,Item
#from db2 import engine, SessionLocal, Base


app = FastAPI()

Base.metadata.create_all(bind=engine)

class ItemSchema(BaseModel):
    name: str
    quantity: int
    price: float


@app.post('/items')
def create_item(item: ItemSchema):
    db = SessionLocal()        
    db_item = Item(name=item.name, quantity=item.quantity, price= item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item

@app.get('/items/{item_id}')
def get_item(item_id: int):
    db= SessionLocal()
    item = db.query(Item).filter(Item.id == item_id).first()
    db.close()
    if not item:
        return {"error": "item not found"}
    return item

@app.put('/items/{item_id}')
def update_item(item_id: int,item: ItemSchema):
    db= SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        db.close()
        return {"error": "item not found"}
    db_item.name =item.name
    db_item.quantity = item.quantity
    db_item.price = item.price
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item

@app.delete('/items/{item_id}')
def delete_item(item_id:int):
    db= SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    
    if not db_item:
        db.close()
        return {"error": "item not found"}
    db.delete(db_item)
    db.commit()
    db.close()
    return {'message': 'item deleted successfully'}