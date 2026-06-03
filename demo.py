import chainlit as cl
from langchain_ollama import ChatOllama

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

    # Initialize the Ollama model
    model = ChatOllama(model="gpt-oss:120b-cloud",base_url="http://127.0.0.1:11434")

    cl.user_session.set("model", model)
    
    # Send a welcome message to the user
    await cl.Message(content="Welcome to the demo!").send()

@cl.on_message
async def main(message: cl.Message):
    """
    This function is called whenever a message is received from the user.
    It calls the tool function and sends the response back to the user.cle
    """

    model = cl.user_session.get("model")
    response = await model.ainvoke(message.content)
    
    await cl.Message(content=response.content).send()