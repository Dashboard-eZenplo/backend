from fastapi import APIRouter, HTTPException

from app.schemas.user import UserBase
from app.services.user_serivce import *

router = APIRouter()


@router.post("/register/")
async def register_user(user: UserBase):
    """
    Route to register a user
    """
    user_db = await get_user_email(user.email)
    if user_db:
        raise HTTPException(status_code=400, detail="User already in database")

    return await process_register(user)


@router.get("/")
async def list_users():
    """
    Route to list all users in the database.
    """
    users = await get_all_users()
    if users:
        return {"users": users}
    else:
        raise HTTPException(status_code=404, detail="No user found")


@router.get("/{id}")
async def get_user(id: int):
    """
    Route to get one user in the database by id
    """
    try:
        user = await get_user_id(id)
        if user:
            return {"users": user}
        else:
            raise HTTPException(status_code=404, detail="No user found")
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
