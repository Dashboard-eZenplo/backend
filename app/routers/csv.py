from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import FileResponse

from app.services.csv_service import process_csv

router = APIRouter()

CSV_BASE_PATH = Path("app/static/template/base_template.csv")


@router.get("/download-csv-template/", response_class=FileResponse)
def download_csv_template():
    """
    Rota para baixar o template de CSV base.
    """
    if not CSV_BASE_PATH.exists():
        raise HTTPException(status_code=404, detail="Template de CSV não encontrado.")

    return FileResponse(
        CSV_BASE_PATH, media_type="text/csv", filename="base_template.csv"
    )


@router.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    """
    Rota para receber e processar um arquivo CSV enviado pelo frontend.
    """
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="O arquivo deve ser um CSV.")

    result = await process_csv(file)
    return {"message": "CSV processado com sucesso", "result": result}
