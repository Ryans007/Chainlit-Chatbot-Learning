# ChatBot Chainlit

Chatbot conversacional com interface web construído com **Chainlit**, **LangGraph** e **LangChain**, rodando modelos locais via **Ollama**.

## Funcionalidades

- Interface de chat web em tempo real
- Memória de conversa por sessão (thread separada por usuário)
- Upload e leitura de arquivos (PDF, TXT, e outros formatos de texto)
- Agente LangGraph com histórico de mensagens

## Exemplos

![Boas-vindas](assets/boas_vindas.jpg)

![Exemplo de conversa](assets/exemplo.jpg)

![Continuação do exemplo](assets/continuacao_exemplo.jpg)

![Guardrail básico](assets/guardrail_basico.jpg)

## Tecnologias

| Tecnologia | Versão | Função |
|---|---|---|
| [Chainlit](https://chainlit.io) | 2.11.1 | Interface web do chat |
| [LangGraph](https://langchain-ai.github.io/langgraph/) | 1.2.4 | Orquestração do agente com estado |
| [LangChain](https://langchain.com) | 1.3.3 | Integração com modelos e ferramentas |
| [langchain-ollama](https://python.langchain.com/docs/integrations/llms/ollama) | 1.1.0 | Conexão com modelos locais via Ollama |
| [pypdf](https://pypdf.readthedocs.io) | 6.12.2 | Extração de texto de arquivos PDF |
| [Ollama](https://ollama.com) | — | Execução local de LLMs |

## Pré-requisitos

- Python 3.10+
- [Ollama](https://ollama.com) instalado e rodando localmente

## Instalação

```bash
# 1. Clone o repositório
git clone <url-do-repositorio>
cd ChatBot-Chainlit

# 2. Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Certifique-se que o Ollama está rodando com o modelo configurado
ollama serve
ollama pull <nome-do-modelo>
```

## Execução

```bash
chainlit run app.py -w --port 8080
```

Acesse `http://localhost:8080` no navegador.

## Estrutura do projeto

```
.
├── app.py          # Ponto de entrada Chainlit (handlers de mensagem)
├── core/
│   ├── agents.py   # Configuração do modelo e agente LangChain
│   ├── graph.py    # Grafo LangGraph com memória
│   ├── nodes.py    # Nó de resposta do grafo
│   └── state.py    # Definição do estado da conversa
├── assets/         # Imagens de exemplo
└── requirements.txt
```
