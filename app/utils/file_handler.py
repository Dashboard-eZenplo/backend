import csv
from pathlib import Path

from fastapi import UploadFile

# Diretório para armazenar arquivos permanentemente
UPLOAD_DIR = Path("app/static/uploads")


async def save_file(file: UploadFile) -> Path:
    """
    Salva o arquivo recebido permanentemente no sistema de arquivos.
    Apaga todos os arquivos existentes na pasta de armazenamento antes de salvar o novo.
    """
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    # Apaga todos os arquivos existentes na pasta de armazenamento permanente
    for existing_file in UPLOAD_DIR.glob("*"):
        if existing_file.is_file():
            existing_file.unlink()

    file_path = UPLOAD_DIR / file.filename

    # Salva o novo arquivo
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())  # Aguarda a leitura do arquivo

    return file_path


def read_csv_file(file_path: Path):
    """
    Lê um arquivo CSV e retorna suas linhas como dicionários.
    """
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
