def chunk_text(text, chunk_size=200, overlap=50):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - overlap
    return chunks


def load_and_chunk(filepath, chunk_size=200, overlap=50):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    return chunk_text(text, chunk_size, overlap)