from rag import search, setup
from llm import generate_answer

setup()

while True:

    q = input("Ask: ")

    context = search(q)

    prompt = f"""
Context: {context}
Question: {q}
Answer:
"""

    ans = generate_answer(prompt)

    print(ans)
