from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
from pathlib import Path
import os


def _get_embeddings():
    return OllamaEmbeddings(
        model="nomic-embed-text",
        base_url="http://127.0.0.1:11434"
    )


def _split_text(text: str) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    return splitter.create_documents([text])


class VectorStore:
    """Gerencia um índice FAISS para uma sessão."""

    def __init__(self, index: FAISS):
        self._index = index

    def as_retriever(self, **kwargs):
        return self._index.as_retriever(**kwargs)

    @classmethod
    def from_text(cls, text: str) -> "VectorStore":
        """Cria um índice a partir de texto já extraído (upload do usuário)."""
        splits = _split_text(text)
        index = FAISS.from_documents(splits, _get_embeddings())
        return cls(index)

    @classmethod
    def from_disk(cls, index_path: Path) -> "VectorStore":
        """Carrega um índice salvo em disco (PDF fixo)."""
        embeddings = _get_embeddings()
        original_dir = os.getcwd()
        os.chdir(index_path.parent)
        index = FAISS.load_local(
            index_path.name,
            embeddings,
            allow_dangerous_deserialization=True
        )
        os.chdir(original_dir)
        return cls(index)