from datetime import timedelta

from fastapi import APIRouter, Depends, Form, HTTPException

from app.schemas.user import UserBase, UserLogin
from app.services.user_service import *
from app.utils.dependencies import get_current_user
from app.utils.jwt_handler import *

# from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/user", tags=["User"])


@router.post("/register/", dependencies=[Depends(get_current_user)])
async def register_user(user: UserBase):
    """
    Route to register a user. Requires authentication.
    """
    user_db = await get_user_email(user.email)
    if user_db:
        raise HTTPException(status_code=400, detail="User already in database")

    response = await process_register(user)
    if response["message"] == "User created successfully":
        access_token = create_access_token(
            data={"sub": user.email},
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        )
        return {
            "message": response["message"],
            "access_token": access_token,
            "token_type": "bearer",
        }

    return response


@router.get("/", dependencies=[Depends(get_current_user)])
async def list_users():
    """
    Route to list all users in the database. Requires authentication.
    """
    users = await get_all_users()
    if users:
        return {"users": users}
    else:
        raise HTTPException(status_code=404, detail="No user found")


@router.get("/{id}", dependencies=[Depends(get_current_user)])
async def get_user(id: int):
    """
    Route to get one user in the database by id. Requires authentication.
    """
    try:
        user = await get_user_id(id)
        if user:
            return {"users": user}
        else:
            raise HTTPException(status_code=404, detail="No user found")
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/login/")
async def login_user(
    email: str = Form(..., description="Email"),
    password: str = Form(..., description="Password"),
):
    """
    Route to login a user. Accessible without a token.
    """
    email = email
    user_password = password

    user = await get_user_password(login.email)

    if not user or not isinstance(user, list) or not isinstance(user[0], tuple):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    stored_password = user[0][0]

    if stored_password == user_password:
        access_token = create_access_token(
            data={"sub": email},
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Invalid email or password")
