from fastapi import FastAPI
from app.routes.documents import router as document_router
from app.routes.auth import router as auth_router
from app.routes.chat import router as chat_router


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

app.include_router(auth_router)

app.include_router(chat_router)