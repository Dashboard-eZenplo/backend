from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from passlib.context import CryptContext
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN

from app.schemas.user import UserBase
from app.services.jwt_service import extract_all_claims
from app.services.user_service import get_user_email

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


async def authenticate_user(email: str, password: str) -> UserBase:
    user = await get_user_email(email)
    if not user or not verify_password(password, user[4]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        claims = extract_all_claims(token)
        user_id = claims.get("user_id")
        admin = claims.get("admin")

        if user_id is None or admin is None:
            raise credentials_exception
        return {"user_id": user_id, "admin": admin}
    except JWTError:
        raise credentials_exception


async def verify_admin(current_user: dict = Depends(get_current_user)):
    if not current_user["admin"]:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action",
        )
    return current_user
