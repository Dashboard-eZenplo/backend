import csv
from pathlib import Path

from fastapi import UploadFile

UPLOAD_DIR = Path("app/static/uploads")


async def save_file(file: UploadFile) -> Path:
    """
    Saves the received file permanently in the file system.
    Deletes all existing files in the storage folder before saving the new one.
    """
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    for existing_file in UPLOAD_DIR.glob("*"):
        if existing_file.is_file():
            existing_file.unlink()

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return file_path


def read_csv_file(file_path: Path):
    """
    Reads a CSV file and returns its rows as dictionaries.
    """
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
