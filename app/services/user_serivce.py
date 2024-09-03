from app.schemas.user import UserCreate


async def process_register(user: UserCreate):
    """
    Processa o usuário, verificando e validando os dados
    """
