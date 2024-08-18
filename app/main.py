from fastapi import FastAPI

from app.routers import csv

app = FastAPI()

app.include_router(csv.router, prefix="/csv", tags=["CSV Operations"])


@app.get("/")
def read_root():
    return {"message": "API FastAPI funcionando!"}
