# api/routes/item.py
from fastapi import APIRouter, HTTPException
from api.utils.logger import log_error, log_info
from api.models.item import Item

router = APIRouter()

fake_items_db = {}

@router.post("/create", response_model=Item)
async def create_item(item: Item):
    if item.id in fake_items_db:
        log_error(f"Item {item.id} already exists.")
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_items_db[item.id] = item
    log_info(f"Item {item.id} created successfully.")
    return item
