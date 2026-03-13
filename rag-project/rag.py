from embed import get_embedding
from pdf_loader import load_pdf

documents = []
doc_embeddings = []


def setup():

    global documents, doc_embeddings

    text = load_pdf("data/sample.pdf")

    documents = text.split("\n")

    doc_embeddings = [get_embedding(d) for d in documents]


def search(query):

    q_emb = get_embedding(query)

    scores = []

    for i, emb in enumerate(doc_embeddings):

        score = sum(a*b for a, b in zip(q_emb, emb))

        scores.append((score, documents[i]))

    scores.sort(reverse=True)

    return scores[0][1]
