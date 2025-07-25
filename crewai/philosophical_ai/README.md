# Setup
## 1. Instale e inicie o Ollama

Se ainda não tiver o Ollama:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Depois, inicie o servidor:
```bash
ollama serve
```

Verifique se está acessível em `http://localhost:11434`.

## 2. Baixe o modelo desejado
Por exemplo, `mistral`:

```bash
ollama pull mistral
```

Outros bons modelos para CrewAI:
* `llama3`
* `phi3`
* `gemma`

## 3. Crie ambiente Python e instale as dependências
Dentro da pasta do seu projeto:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install crewai langchain python-dotenv
```

## 4. Crie um setup para integrar CrewAI com Ollama

Crie o arquivo `ollama_setup.py` com o seguinte conteúdo:
```python
from langchain.chat_models import ChatOllama
from crewai import CrewSettings

llm = ChatOllama(
    model="mistral",  # ou "llama3", "phi3", etc
    temperature=0.7
)

CrewSettings.llm = llm
```


## 5. Adapte o seu código principal
No seu `main.py`, **adicione esse import** logo no início:
```python
from ollama_setup import llm
```

## 6. Estrutura recomendada do projeto
```
philosophy_agents/
├── main.py
├── ollama_setup.py
├── .env                (opcional, se quiser usar variáveis)
├── requirements.txt    (use `pip freeze > requirements.txt`)
└── .venv/
```

## 7. Execute seu projeto
Com tudo configurado, e Ollama rodando:
```bash
python main.py
```

## Observações
* O Ollama não requer `API Key`, nem autenticação.
* O `ChatOllama` da LangChain simula a API OpenAI, então funciona com CrewAI.
* Pode-se usar `temperature=0.0` para respostas mais objetivas, ou `0.7+` para mais criatividade.

## Requisitos mínimos de máquina
Para rodar bem com **Ollama + CrewAI**:
| Recurso   | Para Mistral / Llama3 8B                  |
| --------- | ----------------------------------------- |
| **RAM**   | 12-16 GB mínimo, ideal 32 GB              |
| **CPU**   | 4-8 núcleos                               |
| **Disco** | 10-30 GB livres por modelo                |
| **GPU**   | Opcional, mas acelera muito (6-8 GB VRAM) |
