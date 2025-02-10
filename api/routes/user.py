# api/routes/user.py
from fastapi import APIRouter, HTTPException
from api.models.user import User
from api.utils.auth import create_access_token, verify_token
from api.utils.logger import log_info
from api.utils.exceptions import UserAlreadyExistsError

router = APIRouter()

fake_users_db = {}

@router.post("/create", response_model=User)
async def create_user(user: User):
    if user.id in fake_users_db:
        raise UserAlreadyExistsError()
    fake_users_db[user.id] = user
    log_info(f"User {user.id} created successfully.")
    return user

@router.post("/login")
async def login(user: User):
    if user.id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    token = create_access_token(data={"sub": user.id})
    log_info(f"User {user.id} logged in.")
    return {"access_token": token}
