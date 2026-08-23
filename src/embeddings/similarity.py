import math

from src.embeddings.embeddings import embed_texts


def cosine_similarity(vector_a: list[float], vector_b: list[float]) -> float:
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same dimensions.")

    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))

    magnitude_a = math.sqrt(sum(a * a for a in vector_a))
    magnitude_b = math.sqrt(sum(b * b for b in vector_b))

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Cannot compare a zero-length vector.")

    return dot_product / (magnitude_a * magnitude_b)


if __name__ == "__main__":
    documents = [
        "Baga Beach is popular for nightlife and water sports.",
        "Palolem Beach is known for a quieter, relaxed atmosphere.",
        "Candolim has restaurants and a long beach.",
        "Anjuna is known for its flea market and nightlife.",
    ]

    query = "I want quiet beaches."

    query_vector = embed_texts([query])[0]
    document_vectors = embed_texts(documents)

    scored_documents = []

    for document, document_vector in zip(documents, document_vectors):
        score = cosine_similarity(query_vector, document_vector)
        scored_documents.append((score, document))

    scored_documents.sort(reverse=True)

    for score, document in scored_documents:
        print(f"{score:.3f} | {document}")