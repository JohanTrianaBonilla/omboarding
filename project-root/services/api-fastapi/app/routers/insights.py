from fastapi import APIRouter, HTTPException
from app.llm.llm_manager import ask_llm
from app.llm.prompt_loader import load_prompt

router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/insight")
def generate_insight(candidate_id: int, version: str = "v1"):
    """
    Genera un insight profesional del candidato usando:
    - prompt versionado
    - uso opcional de tools
    """

    try:
        # 1. Cargar prompt versionado
        prompt_template = load_prompt("candidate_summary", version)

        # 2. Reemplazar variable del prompt
        final_prompt = prompt_template.replace("{{candidate_id}}", str(candidate_id))

        # 3. Enviar prompt al LLM (usa tools automáticamente)
        result = ask_llm(final_prompt)

        return {
            "candidate_id": candidate_id,
            "version": version,
            "insight": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
