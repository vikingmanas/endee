
from fastapi import FastAPI
from rag import setup, search
from llm import generate_answer

app = FastAPI()

setup()


@app.get("/ask")
def ask(q: str):

    context = search(q)

    prompt = f"""
Context: {context}
Question: {q}
Answer:
"""

    ans = generate_answer(prompt)

    return {"answer": ans}
