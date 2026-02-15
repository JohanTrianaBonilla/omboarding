from fastapi import APIRouter
import requests
import os

router = APIRouter()

FLASK_SEARCH_URL = os.getenv("FLASK_SEARCH_URL")

@router.post("/semantic-search")
def semantic_search(query: str):
    # Enviar la consulta a Flask
    response = requests.post(
        FLASK_SEARCH_URL,
        json={"query": query}
    )
    
    if response.status_code != 200:
        return {"error": "Flask search failed"}

    return {"results": response.json()}
