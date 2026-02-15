import requests
import os 

FASTAPI_URL = os.getenv("FASTAPI_URL", "http://localhost:8000")
FLASK_URL = os.getenv("FLASK_URL", "http://localhost:5001")

def get_candidate_profile(candidate_id: int):
    response = requests.get(f"{FASTAPI_URL}/candidates/{candidate_id}")
    if response.status_code != 200:
        return {"error": "Candidate not found"}
    return response.json()


def search_similar_profiles(query: str):
    response = requests.get(f"{FLASK_URL}/search?q={query}")
    if response.status_code != 200:
        return {"error": "Search failed"}
    return response.json()


def calculate_score(candidate_text: str, job_description: str):
    candidate_words = set(candidate_text.lower().split())
    job_words = set(job_description.lower().split())

    match = candidate_words.intersection(job_words)
    total = len(job_words)

    score = round((len(match) / total) * 100, 2) if total > 0 else 0

    return {
        "score": score,
        "matching_words": list(match)
    }
