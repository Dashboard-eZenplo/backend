from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.services.user_service import get_user_email
from app.utils.jwt_handler import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login/")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    user = await get_user_email(payload.get("sub"))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
