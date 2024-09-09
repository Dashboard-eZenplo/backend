from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import init_db
from app.routers import csv, login, user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=["*"],
)


def init_app(app: FastAPI) -> None:
    """Initializes the application's routes."""
    init_db()
    app.include_router(user.router)
    app.include_router(csv.router)
    app.include_router(login.router)


init_app(app)
