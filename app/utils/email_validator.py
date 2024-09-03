import re


def email_validator(email):
    """
    Função para validar a estrutura do e-mail
    """
    regex = r"^[a-z0-9.]+@[a-z0-9]+\.[a-z]+(\.[a-z]+)?$"

    if not re.fullmatch(regex, email):
        raise ValueError("E-mail nao esta dentro dos padroes")

    return email
