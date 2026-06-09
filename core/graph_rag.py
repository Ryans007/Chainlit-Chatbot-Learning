from core.nodes import response, rag
from core.state import AgentState
from langgraph.graph import StateGraph, END, START
from langgraph.checkpoint.memory import InMemorySaver  

memory = InMemorySaver()

builder = StateGraph(AgentState)

builder.add_node("response", response)
builder.add_node("rag", rag)

builder.add_edge(START, "rag")
builder.add_edge("rag", "response")
builder.add_edge("response", END)

graph = builder.compile(checkpointer=memory)


if __name__ == "__main__":
    result = graph.invoke({
        "messages": [
            {"role": "user", "content": "Ola, tudo bem?"}
        ]
    }, config={"configurable": {"thread_id": 1234}})

    print(result["messages"][-1].content)