from sentence_transformers import SentenceTransformer

_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def embed_chunks(chunks):
    model = get_model()
    embeddings = model.encode(chunks)
    return embeddings.tolist()


def embed_query(query):
    model = get_model()
    embedding = model.encode([query])
    return embedding.tolist()[0]