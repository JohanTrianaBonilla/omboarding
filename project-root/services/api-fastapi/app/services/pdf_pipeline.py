from __future__ import annotations

import re
from pathlib import Path

import pdfplumber
import requests


def extract_text_from_pdf(pdf_path: str) -> str:
    full_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            full_text += f"{page_text}\n"

    return full_text.strip()


def transform_candidate_text(text: str) -> dict:
    cleaned = re.sub(r"\s+", " ", text).strip()
    name = cleaned.split(" ")[0] if cleaned else "Unknown"

    skills = []
    keywords = ["python", "java", "fastapi", "docker", "sql", "react", "aws", "linux"]

    for keyword in keywords:
        if keyword in cleaned.lower():
            skills.append(keyword)

    years_exp = None
    exp_match = re.search(r"(\d+)\s+años? de experiencia", cleaned.lower())
    if exp_match:
        years_exp = int(exp_match.group(1))

    return {
        "name": name,
        "skills": skills,
        "experience": years_exp,
        "raw_text": cleaned,
    }


def load_candidate(candidate: dict, fastapi_url: str, flask_embed_url: str) -> dict:
    candidate_response = requests.post(
        f"{fastapi_url.rstrip('/')}/candidates/",
        json={
            "name": candidate["name"],
            "skills": ", ".join(candidate["skills"]),
            "experience": candidate["experience"],
        },
        timeout=30,
    )
    candidate_response.raise_for_status()
    candidate_id = candidate_response.json()["id"]

    embed_response = requests.post(
        flask_embed_url,
        json={"candidate_id": candidate_id, "text": candidate["raw_text"]},
        timeout=60,
    )
    embed_response.raise_for_status()

    return {"id": candidate_id, "embedding": embed_response.json()}


def process_pdf(file_path: str, fastapi_url: str, flask_embed_url: str) -> dict:
    resolved = Path(file_path)
    text = extract_text_from_pdf(str(resolved))
    transformed = transform_candidate_text(text)
    return load_candidate(transformed, fastapi_url=fastapi_url, flask_embed_url=flask_embed_url)
