from app.core.database import *
from app.schemas.user import UserBase
from app.utils.validators import *


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

    return await create_user(user)


async def create_user(user: UserBase):
    """
    Creates the user in the database.
    """
    insert_query = """
    INSERT INTO ages.user (name, email, password, cnpj, phone, admin)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    user_data = (
        user.name,
        user.email,
        user.password,
        user.cnpj,
        user.phone,
        user.admin,
    )

    success = insert_data(insert_query, user_data)

    return {
        "message": "User created successfully"
        if success
        else "Error while creating user"
    }


async def get_all_users():
    """
    Get all users from the database.
    """
    query = "SELECT * FROM ages.user"

    return await fetch_data(query)


async def get_user_id(id: int):
    """
    Get a user from the database.
    """
    query = "SELECT * FROM ages.user WHERE id = %s"

    return await fetch_data(query, (id,))


async def get_user_email(email: str):
    """
    Get a user by email from the database.
    """
    query = "SELECT * FROM ages.user WHERE email = %s"

    return await fetch_data(query, (email,))


async def get_user_password(email: str):
    """
    Get a user password by email from the database.
    """
    query = "SELECT password FROM ages.user WHERE email = %s"

    return await fetch_data(query, (email,))
