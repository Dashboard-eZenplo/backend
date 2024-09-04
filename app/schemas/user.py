from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str = Field(..., example="John Doe")
    cnpj: str = Field(..., example="12.345.678/0001-95")
    phone: str = Field(..., example="55999224455")
    email: str = Field(..., example="johndoe@example.com")
    password: str = Field(..., example="strongpassword123")
    admin: bool | None = Field(default=False, example=False)


class User(UserBase):
    id: int = Field(..., example=1)
