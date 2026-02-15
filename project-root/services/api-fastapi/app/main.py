from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import candidates, search, insights
from app.routers.upload import router as upload_router
from app.core.database import init_db
from dotenv import load_dotenv



load_dotenv()



app = FastAPI(title="Candidate Intelligence API")


# ----------------------------------------
# Routers
# ----------------------------------------
app.include_router(candidates.router, prefix="/candidates", tags=["Candidates"])
app.include_router(search.router, prefix="/search", tags=["Semantic Search"])
app.include_router(insights.router, prefix="/insights", tags=["Insights"])
app.include_router(upload_router, prefix="/files", tags=["PDF Upload"])


# ----------------------------------------
# CORS CONFIG
# ----------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # permitido durante desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ----------------------------------------
# Startup
# ----------------------------------------
@app.on_event("startup")
async def startup_event():
    await init_db()


# ----------------------------------------
# Root
# ----------------------------------------
@app.get("/")
def read_root():
    return {"message": "FastAPI is running 🚀"}
