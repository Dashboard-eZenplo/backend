from fastapi import APIRouter

from app.schemas.user import UserBase
from app.services.user_serivce import get_all_users, process_register

router = APIRouter()


@router.post("/register/")
async def register_user(user: UserBase):
    """
    Register user route
    """

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
        return {"message": "No users found or error fetching users"}
