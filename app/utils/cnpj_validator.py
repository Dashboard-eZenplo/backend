import re


async def cnpj_validator(cnpj):
    """
    Função para validar o CNPJ
    Valida tanto o tamanho quanto os dígitos verificadores
    """
    cnpj = re.sub(r"\D", "", cnpj)

    if len(cnpj) != 14:
        raise ValueError("CNPJ deve conter 14 dígitos.")

    def calculate_digit(cnpj, w, second):
        result = sum(int(cnpj[i]) * w[i] for i in range(len(w)))
        digit = 11 - (result % 11)

        return digit if digit >= 2 or second else 0

    weight = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    val1 = calculate_digit(cnpj[:12], weight, False)

    weight.insert(0, 6)
    val2 = calculate_digit(cnpj[:12] + str(val1), weight, True)

    if int(cnpj[12]) != val1 or int(cnpj[13]) != val2:
        raise ValueError(
            "Índices verificadores do CNPJ não estão de acordo com a norma."
        )

    return cnpj
