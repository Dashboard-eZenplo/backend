from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str = Field(..., example="User")
    cnpj: str = Field(..., example="12345678000195")
    phone: str = Field(..., example="55912345678")
    email: str = Field(..., example="user@example.com")
    password: str = Field(..., example="strongpassword123")
    admin: bool | None = Field(default=False, example=False)


class UserLogin(BaseModel):
    email: str = Field(..., example="joao.silva@ezenplo.com")
    password: str = Field(..., example="senha123")


class User(UserBase):
    id: int = Field(..., example=1)
