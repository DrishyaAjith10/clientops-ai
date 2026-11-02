from app.database import SessionLocal
from app.models import Document
from app.services.embeddings import generate_embeddings
from app.services.vector_store import collection

BATCH_SIZE = 500

def ingest_documents():

    db = SessionLocal()

    try:
        query = (
            db.query(Document)
            .order_by(Document.id)
            .yield_per(BATCH_SIZE)
        )

        batch = []

        for doc in query:
            batch.append(doc)

            if len(batch) == BATCH_SIZE:
                process_batch(batch)
                batch = []

        if batch:
            process_batch(batch)

        print("Total vectors:", collection.count())

    finally:
        db.close()


def process_batch(batch):

    ids = [str(doc.id) for doc in batch]

    texts = [
        f"Question: {doc.instruction}\nAnswer: {doc.response}"
        for doc in batch
    ]

    metadatas = [
        {
            "category": doc.category,
            "intent": doc.intent,
            "flags": doc.flags or ""
        }
        for doc in batch
    ]

    embeddings = generate_embeddings(texts)

    collection.upsert(
        ids=ids,
        documents=texts,
        metadatas=metadatas,
        embeddings=embeddings
    )

    print(f"Processed {len(batch)} records")


if __name__ == "__main__":
    ingest_documents()