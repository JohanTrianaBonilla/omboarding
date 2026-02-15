import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
PROMPT_PATH = os.path.join(BASE_PATH, "prompts")

def load_prompt(folder: str, version: str = "v1"):
    """
    Carga un prompt versionado desde /llm/prompts/<folder>/<version>.txt
    """
    filename = f"{version}.txt"
    full_path = os.path.join(PROMPT_PATH, folder, filename)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"El prompt '{folder}/{filename}' no existe en {full_path}")

    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()
