from fastapi import APIRouter

from app.schemas.user import UserBase
from app.services.user_serivce import process_register

router = APIRouter()


@router.post("/register/")
async def register_user(user: UserBase):
    """
    Register user route
    """

    return await process_register(user)
