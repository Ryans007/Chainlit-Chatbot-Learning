from typing import Annotated, TypedDict
from langchain_core.messages import AnyMessage
import operator


class AgentState(TypedDict):
    """State of an agent, which can be used to store any information that the agent needs to function."""

    messages: Annotated[list[AnyMessage], operator.add]