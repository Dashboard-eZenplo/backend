from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    cnpj: str
    phone: str
    email: str
    password: str
    admin: bool | None = False


class User(UserBase):
    id: int
