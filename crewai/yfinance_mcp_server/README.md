# Multi-Agent Analyst – AI Chat Interface

This project is a Streamlit-powered chat interface that connects to a local multi-agent system (FastMCP) capable of answering **financial** and **database-related** questions using **YFinance** and **Supabase** tools, with **per-user memory** powered by OpenAI embeddings.

## Features

- Intelligent agent using `CrewAI` and `LangChain`
- Financial queries via YFinance MCP tool
- Database queries via Supabase MCP tool
- Per-user memory with RAG storage (OpenAI embeddings)
- Interactive chat UI built with Streamlit
- Tool orchestration through `FastMCP`

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/lorenzouriel/ai-agent-with-fastmcp.git
cd ai-agent-with-fastmcp
```

### 2. Install Dependencies
> Ensure Python 3.10+ is installed

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables
Create a `.env` file in the root directory with the following content:
```env
OPENAI_API_KEY=your-openai-api-key
SUPABASE_ACCESS_TOKEN=your-supabase-access-token
```

### 4. Start the FastMCP Server
```bash
python src/mcp_server.py
```

This runs the backend multi-agent system on:
- `http://127.0.0.1:8005/sse`


### 5. Start the Streamlit Frontend
In a **new terminal** tab:
```bash
streamlit run src/streamlit_app.py
```

This launches the chat UI on:
- `http://localhost:8501`

## Example Usage
* Ask: `What is the current price of AAPL?`
* Ask: `Create a table and add the stock data from AAPL`
* Ask: `What was Amazon's stock performance over the past year?`

The system automatically chooses the best tool and formats the response as:
* A table (via pandas)
* JSON output
* Plain text

## Notes
* You must have Node.js installed to run the Supabase and YFinance MCP tools via `npx`.
* The memory is stored per-user using UUIDs and RAG with OpenAI embeddings.
* Compatible with `gpt-4.1-mini` and `text-embedding-3-small`.

---

# Analista Multiagente – Interface de Bate-papo com IA

Este projeto é uma interface de bate-papo com tecnologia Streamlit que se conecta a um sistema multiagente local (FastMCP) capaz de responder a perguntas **financeiras** e **relacionadas a bancos de dados** usando as ferramentas **YFinance** e **Supabase**, com **memória por usuário** alimentada por embeddings OpenAI.

##Recursos

- Agente inteligente usando `CrewAI` e `LangChain`
- Consultas financeiras via ferramenta YFinance MCP
- Consultas a banco de dados via ferramenta Supabase MCP
- Memória por usuário com armazenamento RAG (embeddings OpenAI)
- Interface de bate-papo interativa criada com Streamlit
- Orquestração de ferramentas via `FastMCP`

## Primeiros passos

### 1. Clonar o repositório
```bash
git clone https://github.com/lorenzouriel/ai-agent-with-fastmcp.git
cd ai-agent-with-fastmcp
```

### 2. Instalar dependências
> Certifique-se de que o Python 3.10+ esteja instalado

```bash
pip install -r requirements.txt
```

### 3. Definir variáveis ​​de ambiente
Crie um arquivo `.env` no diretório raiz com o seguinte conteúdo:
```env
OPENAI_API_KEY=sua-chave-api-openai
SUPABASE_ACCESS_TOKEN=seu-token-de-acesso-supabase
```

### 4. Inicie o Servidor FastMCP
```bash
python run src/mcp_server.py
```

Isso executa o sistema multiagente de backend em:
- `http://127.0.0.1:8005/sse`

### 5. Inicie o Frontend Streamlit
Em uma **nova aba de terminal**:
```bash
streamlit run src/streamlit_app.py
```

Isso inicia a interface de bate-papo em:
- `http://localhost:8501`

## Exemplo de Uso
* Pergunta: `Qual é o preço atual da AAPL?`
* Pergunta: `Crie uma tabela e adicione os dados da ação da AAPL`
* Pergunta: `O que Qual foi o desempenho das ações da Amazon no último ano?

O sistema escolhe automaticamente a melhor ferramenta e formata a resposta como:
* Uma tabela (via pandas)
* Saída JSON
* Texto simples

## Observações
* É necessário ter o Node.js instalado para executar as ferramentas Supabase e YFinance MCP via `npx`.
* A memória é armazenada por usuário usando UUIDs e RAG com embeddings OpenAI.
* Compatível com `gpt-4.1-mini` e `text-embedding-3-small`.