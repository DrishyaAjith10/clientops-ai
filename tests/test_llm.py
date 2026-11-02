from app.services.generation import generate_answer

question = "How can I track my order?"

context = [
    {
        "document": """
        Question: Where is my order?

        Answer: You can track your order through
        the Order Tracking section on our website.
        """
    }
]

answer = generate_answer(question, context)

print("Question:", question)
print("Answer:", answer)