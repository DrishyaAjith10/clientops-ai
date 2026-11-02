from app.services.retriever import retrieve_documents
from app.services.generation import generate_answer


def rag_pipeline(question: str, top_k: int = 3):

    # Step 1: Retrieve relevant records
    retrieved_docs = retrieve_documents(
        query=question,
        top_k=top_k
    )

    # Step 2: Generate answer using retrieved context
    answer = generate_answer(
        question=question,
        retrieved_docs=retrieved_docs
    )

    # Step 3: Prepare source references
    sources = []

    for doc in retrieved_docs:
        sources.append({
            "id": doc["id"],
            "category": doc["metadata"]["category"],
            "intent": doc["metadata"]["intent"],
            "distance": doc["distance"]
        })

    return {
        "answer": answer,
        "sources": sources
    }