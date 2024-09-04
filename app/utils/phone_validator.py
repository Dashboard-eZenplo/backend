import re


async def phone_validator(phone):
    """
    Function to validate the structure of the phone number.
    """
    phone = re.sub(r"\D", "", phone)

    if len(phone) != 11:
        return "Phone number has an incorrect number of digits."

    regex = r"^[1-9]{2}9[0-9]{8}$"

    if not re.fullmatch(regex, phone):
        return "Phone number is not in the correct format."

    return None
