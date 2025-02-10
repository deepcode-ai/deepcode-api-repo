# api/models/user.py
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    full_name: Optional[str] = None

    class Config:
        orm_mode = True  # Enables automatic data conversion from ORM models
