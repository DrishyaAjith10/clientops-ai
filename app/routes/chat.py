from fastapi import APIRouter, Depends, HTTPException
from app.schemas_chat import ChatRequest, ChatResponse
from app.services.rag import rag_pipeline
from app.security import get_current_user
from app.models import User

router = APIRouter(
    prefix="/chat",
    tags=["AI Assistant"]
)


@router.post("/", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    current_user: User = Depends(get_current_user)
):
    try:
        result = rag_pipeline(request.question)

        return result

    except Exception as e:
        print("RAG pipeline error:", str(e))

        raise HTTPException(
            status_code=502,
            detail="Unable to generate an answer currently"
        )