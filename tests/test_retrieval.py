from app.services.retriever import retrieve_documents

queries = [
    "Where is my order?",
    "How do I get my money back?",
    "I want to cancel my purchase",
    "I cannot log into my account"
]

for query in queries:
    print("\nQUERY:", query)

    results = retrieve_documents(query, top_k=3)

    for result in results:
        print(result["metadata"]["intent"], result["distance"])