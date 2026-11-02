from app.services.embeddings import generate_embedding
from app.services.vector_store import collection


def retrieve_documents(query: str, top_k: int = 3):

    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )

    retrieved_docs = []

    for i in range(len(results["ids"][0])):

        retrieved_docs.append({
            "id": results["ids"][0][i],
            "document": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "distance": results["distances"][0][i]
        })

    return retrieved_docs