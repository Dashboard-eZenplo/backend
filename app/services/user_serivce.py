from app.schemas.user import UserBase
from app.utils.cnpj_validator import cnpj_validator
from app.utils.database import fetch_data, insert_data
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

    return await create_user(user)


async def create_user(user: UserBase):
    """
    Creates the user in the database.
    """
    insert_query = """
    INSERT INTO users (name, cnpj, phone, email, password, admin)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    user_data = (
        user.name,
        user.cnpj,
        user.phone,
        user.email,
        user.password,
        user.admin,
    )

    success = insert_data(insert_query, user_data)

    if success:
        return {"message": "User created successfully"}
    else:
        return {"message": "Error while creating user"}


async def get_all_users():
    """
    Get all users from the database.
    """
    query = "SELECT * FROM users"
    return await fetch_data(query)
