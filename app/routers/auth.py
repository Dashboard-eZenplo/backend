from fastapi import APIRouter, HTTPException
from jose import JWTError

from app.schemas.auth import LoginRequest, RefreshRequest
from app.services.auth_service import authenticate_user
from app.services.jwt_service import *
from app.services.user_service import get_user_email

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login/")
async def auth(request: LoginRequest):
    email = request.email
    password = request.password

    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and password are required")

    user = await authenticate_user(email, password)

    access_token = generate_token({"email": user[2], "id": user[0], "admin": user[6]})
    refresh_token = generate_refresh_token({"email": user[2]})

    return {"access_token": access_token, "refresh_token": refresh_token}


@router.post("/refresh/")
async def refresh_token(request: RefreshRequest):
    refresh_token = request.refresh_token

    if not refresh_token:
        raise HTTPException(status_code=400, detail="Refresh token is required")
    claims = extract_all_claims(refresh_token)

    try:
        claims = extract_all_claims(refresh_token)
        email = claims.get("sub")

        if is_token_expired(refresh_token):
            raise HTTPException(
                status_code=401, detail="Refresh token has expired, please login again"
            )

        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        user = await get_user_email(email)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        new_access_token = generate_token(
            {"email": email, "id": user[0], "admin": user[6]}
        )

        return {"access_token": new_access_token}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")
