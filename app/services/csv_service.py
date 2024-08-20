from fastapi import HTTPException, UploadFile

from app.utils.file_handler import read_csv_file, save_file


async def process_csv(file: UploadFile):
    """
    Processa o arquivo CSV enviado, valida os dados e retorna os resultados.
    """
    file_path = await save_file(file)  # Salva o arquivo

    try:
        rows = read_csv_file(file_path)

        if len(rows) == 0:
            raise HTTPException(
                status_code=422, detail="CSV inválido. O arquivo deve conter dados."
            )

        required_columns = ["Name", "Age", "Email"]  # TODO - Seria bom tornar dinâmico
        if not all(key in rows[0].keys() for key in required_columns):
            raise HTTPException(
                status_code=422, detail="CSV inválido. Colunas obrigatórias ausentes."
            )

        return rows

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro {str(e)} ao processar o CSV."
        )
