from fastapi import APIRouter

from app.schemas.user import UserBase
from app.services.user_serivce import process_register

router = APIRouter()


@router.post("/register/")
async def register_user(user: UserBase):
    """
    Rota para cadastrar um novo usuário
    """

    result = await process_register(user)
    return {"message": "Usuário cadastrado com sucesso", "result": result}
