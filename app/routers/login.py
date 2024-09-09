from fastapi import APIRouter, HTTPException

from app.services.user_service import *

router = APIRouter(tags=["Login"])


@router.get("/signin/")
async def login_user(email: str, password: str):
    """
    Route to login a user
    """

    user = await get_user_password(email)

    if not user or not isinstance(user, list) or not isinstance(user[0], tuple):
        raise HTTPException(status_code=404, detail="Invalid email or password")

    user_password = user[0][0]

    if user_password == password:
        return {"message": "User successfully logged in"}
    else:
        raise HTTPException(status_code=400, detail="Invalid email or password")
