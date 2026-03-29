# RAG Project 101 🧠

A from-scratch implementation of a **Retrieval-Augmented Generation (RAG)** system built without high-level frameworks like LangChain. Each component is built and tested independently so you can understand exactly what is happening at every step.

---

## What is RAG?

RAG stands for **Retrieval-Augmented Generation**. Instead of relying on the LLM's training data alone, RAG first retrieves relevant information from your own documents and feeds it to the LLM as context — resulting in grounded, accurate answers.

```
Your Documents → Chunks → Vectors → Vector DB
                                         ↓
User Question → Embed → Search Vector DB → Retrieve Chunks
                                                    ↓
                              Chunks + Question → LLM → Answer
```

---

## Tech Stack

| Component | Tool |
|-----------|------|
| Language | Python 3.13 |
| Embedding Model | sentence-transformers (all-MiniLM-L6-v2) |
| Vector Database | ChromaDB |
| LLM | Llama 3 via Ollama (runs locally) |
| PDF Reading | pypdf |

---

## Project Structure

```
rag_project_101/
│
├── document.txt        # Your source document (knowledge base)
├── 01_chunk.py         # Step 1 — Read and chunk the document
├── 02_embed.py         # Step 2 — Convert chunks to vectors
├── 03_store.py         # Step 3 — Store in ChromaDB and test retrieval
├── 04_rag.py           # Step 4 — Full pipeline with Ollama LLM
└── README.md           # This file
```

---

## Prerequisites

Make sure the following are installed on your machine:

- [Python 3.9+](https://python.org)
- [Ollama](https://ollama.com) with Llama 3 pulled:
  ```bash
  ollama pull llama3
  ```

---

## Setup

**1. Clone the repository**
```bash
git clone https://github.com/kaushikkesani/rag_project_101.git
cd rag_project_101
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**3. Install dependencies**
```bash
pip install sentence-transformers chromadb pypdf ollama
```

**4. Add your document**

Place your text file in the project folder and name it `document.txt`

---

## Running the Pipeline

Run each script in order to understand each component:

```bash
# Step 1 — See how the document is chunked
python 01_chunk.py

# Step 2 — See what an embedding (vector) looks like
python 02_embed.py

# Step 3 — Test retrieval without the LLM
python 03_store.py

# Step 4 — Full RAG pipeline (asks for your question interactively)
python 04_rag.py
```

---

## How It Works

### Ingestion (runs once)
1. `document.txt` is read and split into overlapping chunks of ~200 words
2. Each chunk is converted to a 384-dimension vector using `sentence-transformers`
3. Vectors are stored in ChromaDB

### Query (runs on every question)
1. Your question is converted to a vector using the same embedding model
2. ChromaDB finds the 3 most similar chunks
3. Retrieved chunks + your question are combined into a prompt
4. Prompt is sent to Llama 3 via Ollama
5. A grounded answer is returned

---

## Key Concepts

**Chunking** — Documents are split into smaller pieces so the most relevant section can be retrieved rather than the entire document.

**Overlap** — Each chunk shares 50 words with the next to prevent important facts being cut at boundaries.

**Embeddings** — Text converted to numbers where similar meanings produce similar numbers — enabling semantic search rather than keyword matching.

**Local LLM** — Ollama runs Llama 3 entirely on your machine. Your data never leaves your network.

---

## Why No LangChain?

This project intentionally avoids high-level frameworks so every step is visible and understandable. Once you understand what each component does, frameworks like LangChain make much more sense.

---

## Next Steps

- [ ] Add PDF support using `pypdf`
- [ ] Persist ChromaDB to disk
- [ ] Support multiple documents
- [ ] Add source citations to answers
- [ ] Build a chat UI with Streamlit

---

## License

MIT
