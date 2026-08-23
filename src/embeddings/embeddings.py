from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


def embed_texts(texts: list[str]) -> list[list[float]]:
    return model.encode(texts).tolist()


if __name__ == "__main__":
    documents = [
        "Baga Beach is popular for nightlife and water sports.",
        "Palolem Beach is known for a quieter, relaxed atmosphere.",
        "Candolim has restaurants and a long beach.",
        "Anjuna is known for its flea market and nightlife.",
    ]

    vectors = embed_texts(documents)

    print("Number of texts:", len(documents))
    print("Vector dimensions:", len(vectors[0]))
    print("First 10 values of the first vector:", vectors[0][:10])