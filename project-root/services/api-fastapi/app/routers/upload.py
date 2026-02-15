from fastapi import APIRouter, UploadFile, File
import os

from pipelines.etl.extract import extract_text_from_pdf
from pipelines.etl.transform import transform
from pipelines.etl.load import load

router = APIRouter()

UPLOAD_FOLDER = "/tmp/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    # Guardar PDF temporalmente
    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # 1. Extraer texto del PDF
    text = extract_text_from_pdf(file_path)

    # 2. Transformar texto → estructura del candidato
    transformed = transform(text)

    # 3. Cargar en FastAPI + Qdrant (vía Flask)
    result = load(transformed)

    return {
        "status": "ok",
        "candidate_id": result["id"],
        "embedding": result["embedding"]
    }
