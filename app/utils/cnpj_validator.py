import re


async def cnpj_validator(cnpj):
    """
    Function to validate the CNPJ.
    Validates both the length and the check digits.
    """
    cnpj = re.sub(r"\D", "", cnpj)

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
        return "CNPJ check digits do not conform to the standard."

    return None
