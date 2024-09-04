from fastapi import HTTPException

from app.schemas.user import UserBase
from app.utils.cnpj_validator import cnpj_validator
from app.utils.email_validator import email_validator
from app.utils.phone_validator import phone_validator


async def process_register(user: UserBase):
    """
    Processa o usuário, verificando e validando os dados
    """

    if not cnpj_validator(user.cnpj):
        raise HTTPException(status_code=400, detail="CNPJ inválido")

    if not email_validator(user.email):
        raise HTTPException(status_code=400, detail="Email inválido")

    if not phone_validator(user.phone):
        raise HTTPException(status_code=400, detail="Telefone inválido")

    result = await create_user(user)
    return result


async def create_user(user: UserBase):
    """
    Cria o usuário no database
    """
