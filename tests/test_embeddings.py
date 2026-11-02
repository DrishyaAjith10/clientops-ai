from app.services.embeddings import generate_embedding

text = "How can I track my order?"

embedding = generate_embedding(text)

print("Embedding:", embedding)
print("Dimensions:", len(embedding))