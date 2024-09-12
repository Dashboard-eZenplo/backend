import secrets
from datetime import datetime, timedelta, timezone

from fastapi import HTTPException
from jose import JWTError, jwt

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 2
REFRESH_TOKEN_EXPIRE_DAYS = 7

SECRET_KEY = secrets.token_urlsafe(32)


def generate_token(user: dict) -> str:
    claims = {
        "sub": user["email"],
        "user_id": user["id"],
        "admin": user["admin"],
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc)
        + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    return jwt.encode(claims, SECRET_KEY, algorithm=ALGORITHM)


def generate_refresh_token(user: dict) -> str:
    claims = {
        "sub": user["email"],
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS),
    }
    return jwt.encode(claims, SECRET_KEY, algorithm=ALGORITHM)


def extract_claim(token: str, claim_name: str) -> str:
    claims = extract_all_claims(token)
    return claims.get(claim_name)


def extract_all_claims(token: str):
    try:
        claims = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return claims
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


def validate_token(token: str, user_email: str) -> bool:
    email = extract_claim(token, "sub")
    return email == user_email and not is_token_expired(token)


def is_token_expired(token: str) -> bool:
    expiration = extract_claim(token, "exp")
    return datetime.now(timezone.utc) > datetime.fromtimestamp(
        expiration, tz=timezone.utc
    )
