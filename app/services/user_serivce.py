from app.schemas.user import UserBase
from app.utils.cnpj_validator import cnpj_validator
from app.utils.email_validator import email_validator
from app.utils.phone_validator import phone_validator


async def process_register(user: UserBase):
    """
    Processes the user by checking and validating the data.
    """
    validations = [
        lambda: cnpj_validator(user.cnpj),
        lambda: email_validator(user.email),
        lambda: phone_validator(user.phone),
    ]

    for validate in validations:
        error = await validate()
        if error:
            return {"message": "Error while validating user", "type": error}

    result = await create_user(user)
    return result


async def create_user(user: UserBase):
    """
    Creates the user in the database.
    """
    return {"message": "Succesfully create user", "type": 201}
