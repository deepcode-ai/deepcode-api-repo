# api/models/base.py
from pydantic import BaseModel
from typing import Optional

# Define a base model if needed
class BaseModelWithId(BaseModel):
    id: Optional[int] = None

    class Config:
        orm_mode = True  # Required for serializing ORM models
