from fastapi import FastAPI 

app = FastAPI(
    title = "PSYS Auth",
    description = "Headless Authentication service using fastapi and rs256",
    version = "0.1"
)

@app.get("/health",tags=["Health"])
def health_check():
    return {"status":"ok"}