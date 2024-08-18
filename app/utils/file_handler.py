import csv
from pathlib import Path

from fastapi import UploadFile

TEMP_DIR = Path("app/static/temp_files")


async def save_temp_file(file: UploadFile) -> Path:
    """
    Salva o arquivo recebido como temporário no sistema de arquivos.
    """
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    temp_file_path = TEMP_DIR / file.filename

    with open(temp_file_path, "wb") as buffer:
        buffer.write(await file.read())

    return temp_file_path


def read_csv_file(file_path: Path):
    """
    Lê um arquivo CSV e retorna suas linhas como dicionários.
    """
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
