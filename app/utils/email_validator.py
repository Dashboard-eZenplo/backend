import re


async def email_validator(email):
    """
    Function to validate the structure of the email.
    """
    regex = r"^[a-z0-9.]+@[a-z0-9]+\.[a-z]+(\.[a-z]+)?$"

    if not re.fullmatch(regex, email):
        return "Invalid email."

    return None
