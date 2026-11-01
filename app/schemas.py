from pydantic import BaseModel, ConfigDict

class DocumentCreate(BaseModel):
    flags: str | None = None
    instruction: str
    category: str
    intent: str
    response: str


class DocumentResponse(DocumentCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
