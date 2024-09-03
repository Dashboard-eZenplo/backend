from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str
    cnpj: str
    email: EmailStr
    phone: str
    admin: bool | None = False


class User(UserBase):
    id: int


class UserCreate(UserBase):
    password: str
