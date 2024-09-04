from fastapi import FastAPI

from app.routers import csv, user

app = FastAPI()

app.include_router(csv.router, prefix="/csv", tags=["CSV Operations"])
app.include_router(user.router, prefix="/register", tags=["Register Operation"])
