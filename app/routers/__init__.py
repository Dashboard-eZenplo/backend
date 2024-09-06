"""
This module contains the application's routes.

The routes should have the least amount of logic possible and should
focus only on receiving requests and calling controllers.
"""
from fastapi import FastAPI

from . import csv, user


def init_app(app: FastAPI) -> None:
    """Initializes the application's routes."""
    app.include_router(user.router)
    app.include_router(csv.router)
