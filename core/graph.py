from core.nodes import response 
from core.state import AgentState
from langgraph.graph import StateGraph, END, START
from langgraph.checkpoint.memory import InMemorySaver  

memory = InMemorySaver()

builder = StateGraph(AgentState)

builder.add_node("response", response)

builder.add_edge(START, "response")
builder.add_edge("response", END)

graph = builder.compile(checkpointer=memory)


if __name__ == "__main__":
    response = graph.invoke({
        "messages": [
            {"role": "user", "content": "Ola, tudo bem?"}
        ]
    }, config={"thread_id": 1234})
    
    print(response["messages"][-1].content)