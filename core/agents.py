from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain_core.messages import SystemMessage


model = ChatOllama(model="gpt-oss:120b-cloud",base_url="http://127.0.0.1:11434")

system_prompt = """Você é um assistente útil e prestativo. Responda às perguntas do usuário de forma clara e concisa."""

agent = create_agent(
    model=model,
    system_prompt=SystemMessage(content=system_prompt),
)

if __name__ == "__main__":
    # Example usage
    response = agent.invoke({
        "messages": [
            {"role": "user", "content": "Qual é a capital da França?"}
        ]
    })
    print(response["messages"][-1].content)

