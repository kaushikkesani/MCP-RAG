import os
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'

from mcp.server.fastmcp import FastMCP
from rag_core.retriever import ask

PERSIST_PATH = "./chromadb_store"

mcp = FastMCP("RAG MCP 101", host="127.0.0.1", port=8000)

@mcp.tool()
def query_documents(question: str) -> str:
    """
    Search the knowledge base and return a grounded answer.
    Use this tool to answer questions about the ingested PDF document.
    """
    return ask(question, persist_path=PERSIST_PATH)

if __name__ == "__main__":
    print("Starting RAG MCP 101 server on http://127.0.0.1:8000")
    mcp.run(transport="sse")