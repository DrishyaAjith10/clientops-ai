from app.services.rag import rag_pipeline

question = "How can I track my package?"

result = rag_pipeline(question)

print("\nQUESTION:", question)
print("\nANSWER:", result["answer"])

print("\nSOURCES:")

for source in result["sources"]:
    print(source)