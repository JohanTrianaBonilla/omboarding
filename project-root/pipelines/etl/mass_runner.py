from fastapi import FastAPI
from pydantic import BaseModel
from extract import extract_text_from_pdf
from transform import transform
from load import load

app = FastAPI()

class PdfPayload(BaseModel):
    file_path: str

@app.post("/run-etl")
def run_etl(payload: PdfPayload):

    text = extract_text_from_pdf(payload.file_path)
    transformed = transform(text)
    result = load(transformed)

    return {
        "status": "ok",
        "candidate_id": result["id"],
        "embedding": result["embedding"]
    }
