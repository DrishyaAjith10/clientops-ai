
from app.services.retriever import retrieve_documents
from app.services.generation import generate_answer

MAX_DISTANCE = 0.5

def rag_pipeline(question: str, top_k: int = 3):
    retrieved_docs = retrieve_documents(query=question, top_k=top_k)

    # Keep only sufficiently relevant documents
    relevant_docs = [
        doc for doc in retrieved_docs
        if doc["distance"] <= MAX_DISTANCE
    ]

    # Fallback if no relevant documents are found
    if not relevant_docs:
        return {
            "answer": "Sorry, I don't have enough relevant information to answer that question.",
            "sources": []
        }

    answer = generate_answer(
        question=question,
        retrieved_docs=relevant_docs
    )

    sources = [
        {
            "id": doc["id"],
            "category": doc["metadata"]["category"],
            "intent": doc["metadata"]["intent"],
            "distance": doc["distance"]
        }
        for doc in relevant_docs
    ]

    return {
        "answer": answer,
        "sources": sources
    }
