from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.database import AsyncSessionLocal
from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate, CandidateUpdate, CandidateOut

router = APIRouter(prefix="/candidates", tags=["Candidates"])

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# CREATE
@router.post("/", response_model=CandidateOut)
async def create_candidate(candidate: CandidateCreate, db: AsyncSession = Depends(get_db)):
    new_candidate = Candidate(**candidate.dict())
    db.add(new_candidate)
    await db.commit()
    await db.refresh(new_candidate)
    return new_candidate

# READ ALL
@router.get("/", response_model=list[CandidateOut])
async def list_candidates(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Candidate))
    return result.scalars().all()

# READ ONE (GET BY ID)
@router.get("/{candidate_id}", response_model=CandidateOut)
async def get_candidate(candidate_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Candidate).where(Candidate.id == candidate_id))
    candidate = result.scalar_one_or_none()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    return candidate

# UPDATE (PUT)
@router.put("/{candidate_id}", response_model=CandidateOut)
async def update_candidate(candidate_id: int, candidate_data: CandidateUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Candidate).where(Candidate.id == candidate_id))
    candidate = result.scalar_one_or_none()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    for key, value in candidate_data.dict(exclude_unset=True).items():
        setattr(candidate, key, value)

    await db.commit()
    await db.refresh(candidate)
    return candidate

# DELETE
@router.delete("/{candidate_id}")
async def delete_candidate(candidate_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Candidate).where(Candidate.id == candidate_id))
    candidate = result.scalar_one_or_none()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    await db.delete(candidate)
    await db.commit()

    return {"message": "Candidate deleted successfully"}
