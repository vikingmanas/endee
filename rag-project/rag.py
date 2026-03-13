from embed import get_embedding

documents = [
    "AI is artificial intelligence",
    "Vector database stores embeddings",
    "RAG means retrieval augmented generation"
]

doc_embeddings = []


def setup():

    global doc_embeddings

    doc_embeddings = [get_embedding(d) for d in documents]


def search(query):

    q_emb = get_embedding(query)

    scores = []

    for i, emb in enumerate(doc_embeddings):

        score = sum(a*b for a, b in zip(q_emb, emb))

        scores.append((score, documents[i]))

    scores.sort(reverse=True)

    return scores[0][1]
