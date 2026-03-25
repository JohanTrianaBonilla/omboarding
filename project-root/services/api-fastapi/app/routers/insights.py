from fastapi import APIRouter, HTTPException

from app.llm.llm_manager import ask_llm
from app.llm.prompt_loader import load_prompt
from app.schemas.insights import InsightRequest

router = APIRouter()


@router.post("/")
def generate_insight(payload: InsightRequest):
    try:
        prompt_template = load_prompt("candidate_summary", payload.version)
        final_prompt = (
            prompt_template.replace("{{candidate_id}}", str(payload.candidate_id))
            .replace("{{job_description}}", payload.job_description)
        )
        result = ask_llm(final_prompt)

        return {
            "candidate_id": payload.candidate_id,
            "version": payload.version,
            "insight": result,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
