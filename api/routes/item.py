# api/routes/item.py
from fastapi import APIRouter, HTTPException
from typing import List
from api.models.item import Item

router = APIRouter()

# Mock database
fake_items_db = {}

# Create a new item
@router.post("/", response_model=Item)
async def create_item(item: Item):
    if item.id in fake_items_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_items_db[item.id] = item
    return item

# Get an item by ID
@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = fake_items_db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Get a list of all items
@router.get("/", response_model=List[Item])
async def list_items():
    return list(fake_items_db.values())

# Update item details
@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_items_db[item_id] = item
    return item

# Delete an item by ID
@router.delete("/{item_id}", response_model=Item)
async def delete_item(item_id: int):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_items_db[item_id]
    return {"message": f"Item {item_id} deleted successfully"}
