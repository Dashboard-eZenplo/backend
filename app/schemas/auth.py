from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    email: str = Field(..., example="joao.silva@ezenplo.com")
    password: str = Field(..., example="senha123")


class RefreshRequest(BaseModel):
    refresh_token: str
