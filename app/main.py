from fastapi import FastAPI 

from contextlib import asynccontextmanager

from app.db.database import Base,engine
from app.db import models

from app.routers.auth import router as auth_router
@asynccontextmanager
async def lifespan(app:FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title = "PSYS Auth",
    description = "Headless Authentication service using fastapi and rs256",
    version = "0.1",
    lifespan=lifespan
)
app.include_router(auth_router)
@app.get("/health",tags=["Health"])
def health_check():
    return {"status":"ok"}