from fastapi import FastAPI
from app.routes.documents import router as document_router

app = FastAPI(
    title="ClientOps AI",
    description="Internal Knowledge Assistant API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to ClientOps AI"}


@app.get("/health")
def check_status():
    return {"status": "healthy"}


app.include_router(document_router)