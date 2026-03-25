import os

import requests
from fastapi import APIRouter, HTTPException

from app.schemas.search import SemanticSearchRequest

router = APIRouter()

FLASK_SEARCH_URL = os.getenv("FLASK_SEARCH_URL")


@router.post("/semantic-search")
def semantic_search(payload: SemanticSearchRequest):
    response = requests.post(
        FLASK_SEARCH_URL,
        json={"query": payload.query},
        timeout=30,
    )

    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Flask search failed")

    return {"results": response.json()}
