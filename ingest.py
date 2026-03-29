import os
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'

from rag_core.pdf_reader import read_pdf
from rag_core.chunker import chunk_text
from rag_core.embedder import embed_chunks
from rag_core.retriever import store_chunks

# ── CONFIG ───────────────────────────────────────────────────────────────────
PDF_PATH     = "business_modeler_ide.pdf"    # ← swap in your PDF filename
PERSIST_PATH = "./chromadb_store"     # matches persist_path in retriever.py
CHUNK_SIZE   = 200
OVERLAP      = 50
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("RAG MCP 101 — Ingest Pipeline")
    print("=" * 50)

    if not os.path.exists(PDF_PATH):
        print(f"\nERROR: Could not find '{PDF_PATH}'")
        print("Update PDF_PATH at the top of this file and try again.")
        exit(1)

    print(f"\n[1/3] Reading PDF: {PDF_PATH}")
    text = read_pdf(PDF_PATH)
    print(f"      Done — {len(text.split())} words extracted")

    print(f"\n[2/3] Chunking text (size={CHUNK_SIZE}, overlap={OVERLAP})")
    chunks = chunk_text(text, CHUNK_SIZE, OVERLAP)
    print(f"      Done — {len(chunks)} chunks created")

    print(f"\n[3/3] Embedding and storing in ChromaDB at '{PERSIST_PATH}'")
    embeddings = embed_chunks(chunks)
    store_chunks(chunks, embeddings, PERSIST_PATH)

    print("\nDone. ChromaDB is saved to disk and ready for mcp_server.py")
