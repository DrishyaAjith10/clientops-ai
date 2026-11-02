import chromadb
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

client = chromadb.PersistentClient(
    path=str(BASE_DIR / "vector_db")
)

collection = client.get_or_create_collection(
    name="customer_support",
    metadata={"hnsw:space": "cosine"}
)