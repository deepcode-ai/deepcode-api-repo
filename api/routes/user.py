# api/routes/user.py
from fastapi import APIRouter, HTTPException
from typing import List
from api.models.user import User

router = APIRouter()

# Mock database
fake_users_db = {}

# Create a new user
@router.post("/", response_model=User)
async def create_user(user: User):
    if user.id in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    fake_users_db[user.id] = user
    return user

# Get a user by ID
@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = fake_users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Get a list of all users
@router.get("/", response_model=List[User])
async def list_users():
    return list(fake_users_db.values())

# Update user details
@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    fake_users_db[user_id] = user
    return user

# Delete a user by ID
@router.delete("/{user_id}", response_model=User)
async def delete_user(user_id: int):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del fake_users_db[user_id]
    return {"message": f"User {user_id} deleted successfully"}
