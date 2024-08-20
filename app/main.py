from fastapi import FastAPI

from app.routers import csv

app = FastAPI()

app.include_router(csv.router, prefix="/csv", tags=["CSV Operations"])
