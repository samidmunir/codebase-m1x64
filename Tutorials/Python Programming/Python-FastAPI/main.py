from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

"""
    GET
    - returning information from the endpoint (read).
    POST
    - sending information to the endpoint (create).
    PUT
    - updating information in the endpoint (update).
    DELETE
    - deleting information from the endpoint (delete).
"""

"""
@app.get('/')
def home():
    return {'Data:': 'Home'} # returning Python dictionary (data)... automatically json.

@app.get('/about')
def about():
    return {'Data': 'About'}
"""

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

inventory = {
    1: {
        'name': 'Milk',
        'price': 3.99,
        'brand': 'Kirkland',
    }
}

@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(description = 'ID of the item to retrieve', gt = 0, lt = 2)):
    return inventory[item_id]

@app.get('/get-by-name')
def get_item_by_name(*, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
    return {'Data': 'Not found'}

@app.get('/get-by-name/{item_id}')
def get_item_by_name(*, item_id: int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
    return {'Data': 'Not found'}

@app.post('/create-item/{item_id}')
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {'Error': 'Item ID already exists'}
    inventory[item_id] = item
    return inventory[item_id]

@app.put('/update-item/{item_id}')
def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        return {'Error': 'Item ID does not exist'}
    if item.name != None:
        inventory[item_id].name = item.name
        
    if item.price != None:
        inventory[item_id].price = item.price
        
    if item.brand != None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]

@app.delete('/delete-item')
def delete_item(item_id: int = Query(..., description = 'ID of item to delete', gt = 0)):
    if item_id not in inventory:
        return {'Error': 'ID does not exist.'}
    del inventory[item_id]
    return {'Success': 'Item deleted!'}