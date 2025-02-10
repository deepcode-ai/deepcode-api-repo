# api/main.py
from fastapi import FastAPI
from api.routes import user, item

app = FastAPI()

# Include the user and item routers
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(item.router, prefix="/items", tags=["items"])
