import requests
import os
from dotenv import load_dotenv

load_dotenv()

FASTAPI_URL = os.getenv("FASTAPI_URL") + "/candidates/"
FLASK_EMBED_URL = os.getenv("FLASK_EMBED_URL")



def load_to_fastapi(candidate: dict) -> int:
    """Guarda el candidato en FastAPI → PostgreSQL."""
    resp = requests.post(FASTAPI_URL, json={
        "name": candidate["name"],
        "skills": ", ".join(candidate["skills"]),
        "experience": candidate["experience"]
    })

    resp.raise_for_status()
    data = resp.json()
    return data["id"]   # ID en PostgreSQL

def load_to_flask_embeddings(candidate_id: int, text: str):
    """Genera embeddings en Flask y los sube a Qdrant."""
    resp = requests.post(FLASK_EMBED_URL, json={
        "candidate_id": candidate_id,
        "text": text
    })
    resp.raise_for_status()
    return resp.json()

def load(candidate: dict):
    """Pipeline de carga."""
    candidate_id = load_to_fastapi(candidate)
    emb_result = load_to_flask_embeddings(candidate_id, candidate["raw_text"])
    return {"id": candidate_id, "embedding": emb_result}
