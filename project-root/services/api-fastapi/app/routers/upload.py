import os
from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas.upload import RunEtlRequest
from app.services.pdf_pipeline import process_pdf

router = APIRouter()

UPLOAD_FOLDER = "/tmp/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

FASTAPI_URL = os.getenv("FASTAPI_URL", "http://localhost:8000")
FLASK_EMBED_URL = os.getenv("FLASK_EMBED_URL", "http://localhost:5001/embed")


@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = Path(UPLOAD_FOLDER) / file.filename

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    result = process_pdf(
        str(file_path),
        fastapi_url=FASTAPI_URL,
        flask_embed_url=FLASK_EMBED_URL,
    )

    return {
        "status": "ok",
        "candidate_id": result["id"],
        "embedding": result["embedding"],
    }


@router.post("/run-etl")
def run_etl(payload: RunEtlRequest):
    file_path = Path(payload.file_path)

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="PDF file not found")

    result = process_pdf(
        str(file_path),
        fastapi_url=FASTAPI_URL,
        flask_embed_url=FLASK_EMBED_URL,
    )

    return {
        "status": "ok",
        "candidate_id": result["id"],
        "embedding": result["embedding"],
    }
