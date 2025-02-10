# api/utils/exceptions.py
from fastapi import HTTPException

class ItemNotFoundError(HTTPException):
    def __init__(self, detail: str = "Item not found"):
        super().__init__(status_code=404, detail=detail)

class UserAlreadyExistsError(HTTPException):
    def __init__(self, detail: str = "User already exists"):
        super().__init__(status_code=400, detail=detail)
