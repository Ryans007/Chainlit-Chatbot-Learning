import chainlit as cl
from core.graph import graph
from langgraph.graph.state import RunnableConfig
from pypdf import PdfReader

import random


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

    for element in message.elements:
        if isinstance(element, cl.File):
            file_text = extract_file_text(element)
            content += f"\n\n[Arquivo: {element.name}]\n{file_text}"

    response = await graph.ainvoke({
        "messages": [{"role": "user", "content": content}]
    }, config=config)

    await cl.Message(content=response["messages"][-1].content).send()