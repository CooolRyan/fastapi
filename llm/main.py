from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI()

class Item(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    price: float
    is_offer: Optional[bool] = None

items = []

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items", response_model=List[Item])
async def read_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: UUID):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: UUID, item: Item):
    for index, existing_item in enumerate(items):
        if existing_item.id == item_id:
            items[index] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: UUID):
    for index, existing_item in enumerate(items):
        if existing_item.id == item_id:
            return items.pop(index)
    raise HTTPException(status_code=404, detail="Item not found")