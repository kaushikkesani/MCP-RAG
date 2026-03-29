import chromadb
import ollama

_client = None
_collection = None

def get_collection(persist_path="./chromadb_store"):
    global _client, _collection
    if _collection is None:
        _client = chromadb.PersistentClient(path=persist_path)
        _collection = _client.get_or_create_collection("rag_docs")
    return _collection


def store_chunks(chunks, embeddings, persist_path="./chromadb_store"):
    collection = get_collection(persist_path)
    ids = [f"chunk_{i}" for i in range(len(chunks))]
    collection.add(documents=chunks, embeddings=embeddings, ids=ids)
    print(f"Stored {len(chunks)} chunks to {persist_path}")


def retrieve(query_embedding, n_results=3, persist_path="./chromadb_store"):
    collection = get_collection(persist_path)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    return results["documents"][0]


def ask(query, n_results=3, persist_path="./chromadb_store"):
    from rag_core.embedder import embed_query
    print(f"[1] Embedding query: {query}", flush=True)
    query_embedding = embed_query(query)
    print(f"[2] Retrieving chunks...", flush=True)
    chunks = retrieve(query_embedding, n_results, persist_path=persist_path)
    print(f"[3] Got {len(chunks)} chunks, calling Ollama...", flush=True)
    context = "\n\n".join(chunks)
    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "system",
                "content": "Answer the question using only the context below. If the answer is not in the context, say 'I don't have enough information'."
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {query}"
            }
        ]
    )
    print(f"[4] Ollama responded.", flush=True)
    return response["message"]["content"]
