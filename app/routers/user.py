from fastapi import APIRouter

from app.schemas.user import UserCreate
from app.services.user_serivce import process_register

router = APIRouter()


@router.post("/register/")
def register_user(user: UserCreate):
    """
    Rota para cadastrar um novo usuário
    """

    result = process_register(user)
    return {"message": "Usuário cadastrado com sucesso", "result": result}
