from fastapi import HTTPException, UploadFile

from app.utils.file_handler import read_csv_file, save_file


async def process_csv(file: UploadFile):
    """
    Processes the uploaded CSV file, validates the data, and returns the results.
    """
    file_path = await save_file(file)

    try:
        rows = read_csv_file(file_path)

        if len(rows) == 0:
            raise HTTPException(
                status_code=422, detail="Invalid CSV. The file must contain data."
            )

        required_columns = ["Name", "Age", "Email"]
        if not all(key in rows[0].keys() for key in required_columns):
            raise HTTPException(
                status_code=422, detail="Invalid CSV. Required columns are missing."
            )

        return rows

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error {str(e)} while processing the CSV."
        )
