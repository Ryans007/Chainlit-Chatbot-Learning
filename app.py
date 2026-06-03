import chainlit as cl
from core.graph import graph
from langgraph.graph.state import RunnableConfig

import random

@cl.step(type="tool")
async def tool():
    await cl.sleep(2)
    return "Response from the tool!"

@cl.on_chat_start
async def start():
    """
    This function is called when the chat starts.
    It initializes the Ollama model and sends a welcome message to the user.
    """
    
    thread_id = random.randint(1, 1000000)
    config = RunnableConfig(configurable={"thread_id": thread_id})
    
    cl.user_session.set("config", config)
    
    # # Send a welcome message to the user
    # await cl.Message(content="Welcome to the demo!").send()

@cl.on_message
async def main(message: cl.Message):
    """
    This function is called whenever a message is received from the user.
    It calls the tool function and sends the response back to the user.cle
    """
    config = cl.user_session.get("config")
    response = await graph.ainvoke({
        "messages": [{"role": "user", "content": message.content}]
    }, config=config)
    
    await cl.Message(content=response["messages"][-1].content).send()