import chainlit as cl
from core.graph import graph as graph_simple
from core.graph_rag import graph as graph_rag
from core.rag.vectorstore import VectorStore
from langgraph.graph.state import RunnableConfig
from pypdf import PdfReader
import random

USE_RAG = True  

graph = graph_rag if USE_RAG else graph_simple


def extract_file_text(element: cl.File) -> str:
    if element.name.lower().endswith(".pdf"):
        reader = PdfReader(element.path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    with open(element.path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


@cl.on_chat_start
async def start():
    thread_id = random.randint(1, 1000000)
    config = RunnableConfig(configurable={"thread_id": thread_id})
    cl.user_session.set("config", config)


@cl.on_message
async def main(message: cl.Message):
    config = cl.user_session.get("config")
    content = message.content
    vectorstore = None

    for element in message.elements:
        if isinstance(element, cl.File):
            file_text = extract_file_text(element)
            if USE_RAG:
                vectorstore = VectorStore.from_text(file_text)
            else:
                content += f"\n\n[Arquivo: {element.name}]\n{file_text}"

    if USE_RAG and vectorstore is not None:
        cl.user_session.set("vectorstore", vectorstore)

    invoke_input = {"messages": [{"role": "user", "content": content}]}

    vs = cl.user_session.get("vectorstore") if USE_RAG else None
    run_config = {**config, "configurable": {**config["configurable"], "vectorstore": vs}}

    response = await graph.ainvoke(invoke_input, config=run_config)
    await cl.Message(content=response["messages"][-1].content).send()