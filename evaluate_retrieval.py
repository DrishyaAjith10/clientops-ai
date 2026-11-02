
from app.services.retriever import retrieve_documents

test_cases = [
    {
        "query": "How can I track my package?",
        "expected_intent": "track_order",
        "relevant_intents": ["track_order", "delivery_period"]
    },
    {
        "query": "How do I get my money back?",
        "expected_intent": "get_refund",
        "relevant_intents": ["get_refund"]
    },
    {
        "query": "I want to cancel my purchase",
        "expected_intent": "cancel_order",
        "relevant_intents": ["cancel_order"]
    },
    {
        "query": "I cannot log into my account",
        "expected_intent": "recover_password",
        "relevant_intents": [
            "recover_password",
            "registration_problems"
        ]
    }
]

K = 3

precision_scores = []
recall_scores = []
reciprocal_ranks = []
hit_scores = []

for test in test_cases:
    results = retrieve_documents(test["query"], top_k=K)

    relevant_intents = test["relevant_intents"]
    expected_intent = test["expected_intent"]

    retrieved_relevant = [
        doc for doc in results
        if doc["metadata"]["intent"] in relevant_intents
    ]

    # Precision@K
    precision = len(retrieved_relevant) / K

    # Recall@K (intent-level proxy)
    recall = len(set(
        doc["metadata"]["intent"] for doc in retrieved_relevant
    )) / len(relevant_intents)

    # MRR
    reciprocal_rank = 0

    for rank, doc in enumerate(results, start=1):
        if doc["metadata"]["intent"] in relevant_intents:
            reciprocal_rank = 1 / rank
            break

    # Hit Rate@K
    hit = 1 if retrieved_relevant else 0

    precision_scores.append(precision)
    recall_scores.append(recall)
    reciprocal_ranks.append(reciprocal_rank)
    hit_scores.append(hit)

    print("\n" + "=" * 55)
    print("Query:", test["query"])
    print("Expected intent:", expected_intent)

    for rank, doc in enumerate(results, start=1):
        print(
            rank,
            doc["metadata"]["intent"],
            f"Distance: {doc['distance']:.4f}"
        )

    print(f"Precision@{K}: {precision:.4f}")
    print(f"Recall@{K}: {recall:.4f}")
    print(f"Reciprocal Rank: {reciprocal_rank:.4f}")
    print(f"Hit Rate@{K}: {hit}")

print("\n" + "=" * 55)
print("OVERALL EVALUATION")

print(f"Mean Precision@{K}: {sum(precision_scores)/len(precision_scores):.4f}")
print(f"Mean Recall@{K}: {sum(recall_scores)/len(recall_scores):.4f}")
print(f"MRR: {sum(reciprocal_ranks)/len(reciprocal_ranks):.4f}")
print(f"Hit Rate@{K}: {sum(hit_scores)/len(hit_scores):.4f}")

print("=" * 55)
