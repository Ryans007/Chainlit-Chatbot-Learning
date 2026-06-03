from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain_core.messages import SystemMessage


model = ChatOllama(model="gpt-oss:120b-cloud",base_url="http://127.0.0.1:11434")

system_prompt = """Você é um assistente especialista em exame de sangue. recebera um pdf de um exame de sangue e respondera
perguntas sobre ele. Se o usuário fizer uma pergunta que não pode ser respondida com base no exame de sangue, responda "Desculpe, não posso responder a essa pergunta com base no exame de sangue fornecido.".
Você pode responder outras perguntas do usuário, mas se ele perguntar de outro documento ou algo aleatório que não seja sobre saude, diga que não pode responder a essa pergunta. Se o usuário fizer uma pergunta sobre o exame de sangue, responda com base nas informações do exame de sangue fornecido. Seja claro e conciso em suas respostas."""

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

