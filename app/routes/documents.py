from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import Query

from app.database import get_db
from app.models import Document
from app.schemas import DocumentCreate, DocumentResponse

from app.security import get_current_user
from app.models import User

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


# CREATE
@router.post("/", response_model=DocumentResponse, status_code=201)
def create_document(
    doc: DocumentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_document = Document(**doc.model_dump())

    try:
        db.add(new_document)
        db.commit()
        db.refresh(new_document)

        return new_document

    except Exception:
        db.rollback()
        raise


# READ ALL

@router.get("/", response_model=list[DocumentResponse])
def get_documents(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    current_user: User = Depends(get_current_user)
    
):
    documents = (
        db.query(Document)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return documents


# READ ONE
@router.get("/{document_id}", response_model=DocumentResponse)
def get_document(document_id: int, 
                 db: Session = Depends(get_db),
                 current_user: User = Depends(get_current_user)):

    doc = db.query(Document).filter(
        Document.id == document_id
    ).first()

    if not doc:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return doc


# UPDATE
@router.put("/{document_id}", response_model=DocumentResponse)
def update_document(
    document_id: int,
    updated_doc: DocumentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    doc = db.query(Document).filter(
        Document.id == document_id
    ).first()

    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    for key, value in updated_doc.model_dump().items():
        setattr(doc, key, value)

    db.commit()
    db.refresh(doc)

    return doc


# DELETE
@router.delete("/{document_id}")
def delete_document(document_id: int,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):

    doc = db.query(Document).filter(
        Document.id == document_id
    ).first()

    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    db.delete(doc)
    db.commit()

    return {"message": "Document deleted successfully"}