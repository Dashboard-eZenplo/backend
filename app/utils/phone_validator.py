import re


def phone_validator(phone):
    """
    Função para validar a estrutura do telefone
    """
    phone = re.sub(r"\D", "", phone)

    if len(phone) != 11:
        raise ValueError("Telefone possui mais digitos que o normal")

    regex = r"^[1-9]{2}9[0-9]{8}$"

    if not re.fullmatch(regex, phone):
        raise ValueError("Telefone nao esta dentro dos padroes")

    return phone
