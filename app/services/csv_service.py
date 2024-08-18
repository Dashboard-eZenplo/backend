from fastapi import UploadFile

from app.utils.file_handler import read_csv_file, save_temp_file


async def process_csv(file: UploadFile):
    """
    Processa o arquivo CSV enviado, valida os dados e retorna os resultados.
    """
    temp_file_path = await save_temp_file(file)

    try:
        rows = read_csv_file(temp_file_path)
        processed_data = []

        for row in rows:
            # Exemplo: Simples validação de campos
            processed_data.append(
                {
                    "name": row.get("name"),
                    "description": row.get("description"),
                    "price": float(row.get("price", 0)),
                    "tax": float(row.get("tax", 0)),
                }
            )

        return processed_data
    finally:
        temp_file_path.unlink()  # Remove o arquivo temporário após o processamento
