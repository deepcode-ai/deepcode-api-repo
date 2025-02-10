# api/models/item.py
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float

    class Config:
        orm_mode = True  # Enables automatic data conversion from ORM models
