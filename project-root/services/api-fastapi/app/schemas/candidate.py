from pydantic import BaseModel

class CandidateBase(BaseModel):
    name: str
    skills: str | None = None
    experience: str | None = None

class CandidateCreate(CandidateBase):
    pass

class CandidateUpdate(CandidateBase):
    pass

class CandidateOut(CandidateBase):
    id: int

    class Config:
        from_attributes = True
