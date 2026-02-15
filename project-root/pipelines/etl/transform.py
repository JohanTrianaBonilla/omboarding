import re

def clean_text(text: str) -> str:
    """Limpia saltos, espacios y caracteres raros."""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_basic_fields(text: str) -> dict:
    """Extrae información básica (nombre, skills, experiencia)."""

    name = text.split(" ")[0] if text else "Unknown"

    skills = []
    keywords = ["python", "java", "fastapi", "docker", "sql", "react", "aws", "linux"]

    for k in keywords:
        if k.lower() in text.lower():
            skills.append(k)

    years_exp = None
    exp_match = re.search(r"(\d+)\s+años? de experiencia", text.lower())
    if exp_match:
        years_exp = int(exp_match.group(1))

    return {
        "name": name,
        "skills": skills,
        "experience": years_exp,
        "raw_text": text
    }

def transform(text: str) -> dict:
    cleaned = clean_text(text)
    return extract_basic_fields(cleaned)
