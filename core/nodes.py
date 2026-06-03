from core.state import AgentState
from core.agents import agent


def response(state: AgentState) -> dict:
    result = agent.invoke({"messages": state["messages"]})
    return {"messages": [result["messages"][-1]]}
    