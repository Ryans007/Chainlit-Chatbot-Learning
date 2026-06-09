from langchain_core.messages import SystemMessage
from langchain_core.runnables import RunnableConfig
from core.state import AgentState
from core.agents import agent


def rag(state: AgentState, config: RunnableConfig) -> dict:
    vectorstore = config.get("configurable", {}).get("vectorstore")
    if vectorstore is None:
        return {"context": ""}

    last_msg = state["messages"][-1]
    query = last_msg.content if hasattr(last_msg, "content") else last_msg["content"]

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(query)
    context = "\n\n".join(
        f"Trecho {i+1}:\n{doc.page_content}" for i, doc in enumerate(docs)
    )
    return {"context": context}


def response(state: AgentState) -> dict:
    messages = state["messages"]
    context = state.get("context", "")

    if context:
        messages = [SystemMessage(content=f"Use o contexto abaixo para responder:\n\n{context}")] + messages

    result = agent.invoke({"messages": messages})
    return {"messages": [result["messages"][-1]]}
    