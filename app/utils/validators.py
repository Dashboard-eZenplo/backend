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


async def email_validator(email):
    """
    Function to validate the structure of the email.
    """
    regex = r"^[a-z0-9.]+@[a-z0-9]+\.[a-z]+(\.[a-z]+)?$"

    if not re.fullmatch(regex, email):
        return "Invalid email."

    return None


async def cnpj_validator(cnpj):
    """
    Function to validate the CNPJ.
    Validates both the length and the check digits.
    """
    if not cnpj.isdigit():
        return "CNPJ must contain only numbers."

    if len(cnpj) != 14:
        return "CNPJ must contain 14 digits."

    def calculate_digit(cnpj, weights, second):
        result = sum(int(cnpj[i]) * weights[i] for i in range(len(weights)))
        digit = 11 - (result % 11)

        return digit if digit >= 2 or second else 0

    weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    val1 = calculate_digit(cnpj[:12], weights, False)

    weights.insert(0, 6)
    val2 = calculate_digit(cnpj[:12] + str(val1), weights, True)

    if int(cnpj[12]) != val1 or int(cnpj[13]) != val2:
        return "Invalid CNPJ."

    return None
