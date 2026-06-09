from langchain_core.tools import tool
from core.rag.vectorstore import VectorStore


@tool
def retrieve_documents_tool(query: str) -> str:
    """Recupera trechos relevantes do índice de documentos com base na consulta."""
    vectorstore = VectorStore.get_instance()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5, "fetch_k": 20})
    docs = retriever.invoke(query)
    results = "\n\n".join(
        f"Documento {i+1}:\n{doc.page_content}" for i, doc in enumerate(docs)
    )
    return results if results else "Nenhum documento encontrado."
