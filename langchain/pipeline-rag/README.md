# Complete RAG Pipeline — Ingestion, Querying & Observability
This project demonstrates a full **Retrieval-Augmented Generation (RAG)** pipeline using:
* **LangChain** — connects LLMs and vector databases
* **LangGraph** — orchestrates nodes and workflow
* **Langfuse** — provides observability and analytics
* **Qdrant** — local vector store
* **Streamlit** — interactive user interface

The demo app answers questions about *TCEMG legal rulings* (Brazilian Court of Accounts) using indexed PDF documents.

## Project Structure
```
rag-project/
├── app/
│   ├── graph/         # LangGraph flow and prompts
│   ├── ingest/        # Text extraction and embeddings
│   ├── retrieval/     # Retriever and query logic
│   ├── app.py         # Streamlit interface
│   └── settings.py    # Global configuration
├── requirements.txt
└── Dockerfile (optional)
```

## Core Concepts
* **RAG (Retrieval-Augmented Generation)** — combines semantic search with LLM generation.
* **Self-Query Retriever** — allows the model to build structured filters automatically.
* **LangGraph** — controls node flow (`retrieve → generate → end`).
* **Langfuse** — tracks executions, tokens, and latency for full visibility.

## Quick Start
**Run Qdrant locally**
```bash
docker run -d -p 6333:6333 qdrant/qdrant
```

**Set environment variables** in a `.env` file:
```
OPENAI_API_KEY=sk-...
LANGFUSE_PUBLIC_KEY=pk-...
LANGFUSE_SECRET_KEY=sk-...
QDRANT_HOST=localhost
QDRANT_PORT=6333
```

**Install dependencies**
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Ingest your documents**
```bash
python app/ingest/extract_text.py
```

**Run the app**
```bash
streamlit run app/app.py
```

Then open: [http://localhost:8501](http://localhost:8501)

## Observability
All executions are tracked via **Langfuse**, showing prompts, context, token usage, and response times.