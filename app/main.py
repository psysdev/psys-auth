from fastapi import FastAPI 

from contextlib import asynccontextmanager

from app.database import Base,engine
from app import models

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

@app.get("/health",tags=["Health"])
def health_check():
    return {"status":"ok"}