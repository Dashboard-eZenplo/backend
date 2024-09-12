from fastapi import APIRouter, Depends, HTTPException

from app.schemas.user import UserBase
from app.services.auth_service import hash_password, verify_admin
from app.services.user_service import *

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/register/")
async def register_user(user: UserBase, admin: dict = Depends(verify_admin)):
    """
    Route to register a user (only admins)
    """
    user_db = await get_user_email(user.email)
    if user_db:
        raise HTTPException(status_code=400, detail="User already in database")

    hashed_password = hash_password(user.password)
    user.password = hashed_password

    return await process_register(user)


@router.get("/")
async def list_users(admin: dict = Depends(verify_admin)):
    """
    Route to list all users in the database.
    """
    users = await get_all_users()
    if users:
        return {"users": users}
    else:
        raise HTTPException(status_code=404, detail="No user found")


@router.get("/{id}")
async def get_user(id: int, admin: dict = Depends(verify_admin)):
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


@router.get("/login/")
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
