# Finance Assistant API
This FastAPI application allows you to extract financial transaction data from natural language messages using a Groq-hosted LLaMA model, save those transactions in a SQLite database, and query them via REST API.

## Features
- Extract amount, category, and date from financial text messages  
- Store transactions in a SQLite database using SQLModel  
- List all transactions  
- Filter transactions by category  
- Ask natural language questions like "Quanto eu gastei com Alimentação?" and get a summarized answer

## Prerequisites
- Python 3.9+  
- SQLite  
- Groq API Key (set as `GROQ_API_KEY` in your `.env`)  

## Setup
1. Clone this repository:
```bash
git clone https://github.com/lorenzouriel/coding-ai-agents.git
cd /no-framework/finance-assistant
```

2. Create and activate a virtual environment:

```bash
uv venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows PowerShell
```

3. Install dependencies:
```bash
uv add fastapi uvicorn python-dotenv sqlmodel openai

# Or

pip install -r requirements.txt
```

4. Create a `.env` file with your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

## Running the app
Start the server with:
```bash
uvicorn main:app --reload
```

On startup, you should see:
```
Banco de dados e tabelas prontos.
INFO:     Uvicorn running on http://127.0.0.1:8000
```

## API Endpoints
### 1. POST `/webhook`
Extract financial data from a message and save it.

* **Request JSON:**
```json
{
  "message": "Gastei 80 reais em alimentação hoje"
}
```

* **Response:**
```json
{
  "reply": "Registrado! 💸 R$80.00 em alimentação (2025-07-09)"
}
```

### 2. GET `/transactions`
Get a list of all stored transactions.

* **Response example:**
```json
[
  {
    "id": 1,
    "message": "Gastei 80 reais em alimentação hoje",
    "amount": 80.0,
    "category": "alimentação",
    "date": "2025-07-09T00:00:00"
  }
]
```

### 3. GET `/transaction/filter?category=alimentação`
Get transactions filtered by category.

* **Example:**
```bash
curl "http://localhost:8000/transaction/filter?category=alimentação"
```

* **Response:**
```json
[
  {
    "id": 1,
    "message": "Gastei 80 reais em alimentação hoje",
    "amount": 80.0,
    "category": "alimentação",
    "date": "2025-07-09T00:00:00"
  }
]
```

### 4. POST `/ask`
Ask a natural language question about your transactions.

* **Request JSON:**
```json
{
  "question": "Quanto eu gastei com alimentação?"
}
```

* **Response:**
```json
{
  "answer": "Você gastou R$80.00 em alimentação."
}
```