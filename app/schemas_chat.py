from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(min_length=2, max_length=1000)


class SourceResponse(BaseModel):
    id: str
    category: str
    intent: str
    distance: float


class ChatResponse(BaseModel):
    answer: str
    sources: list[SourceResponse]