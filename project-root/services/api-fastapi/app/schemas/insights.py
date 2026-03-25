from pydantic import BaseModel


class InsightRequest(BaseModel):
    candidate_id: int
    job_description: str
    version: str = "v1"
