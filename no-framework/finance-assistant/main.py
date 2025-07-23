from fastapi import FastAPI, Request, Query, HTTPException, Body
from typing import List
from dotenv import load_dotenv
from openai import OpenAI
from db import get_session, create_db_and_tables
from models import Transaction
import os
import json
from datetime import datetime
from sqlmodel import select
from sqlalchemy import func

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    print("Banco de dados e tabelas prontos.")

@app.get("/transactions", response_model=List[Transaction])
def list_transactions():
    with get_session() as session:
        transactions = session.exec(select(Transaction)).all()
    return transactions

@app.get("/transaction/filter", response_model=List[Transaction])
def filter_transactions(category: str = Query(..., description="Category to filter by")):
    with get_session() as session:
        transactions = session.query(Transaction).where(Transaction.category == category).all()
    if not transactions:
        raise HTTPException(status_code=404, detail="No transactions found for this category")
    return transactions

@app.post("/ask")
async def ask_question(payload: dict = Body(...)):
    question = payload.get("question", "")

    known_categories = ["alimentação", "transporte", "poupança", "outro"]

    matched_category = None
    for cat in known_categories:
        if cat in question:
            matched_category = cat
            break

    if not matched_category:
        return {"answer": "Não entendi a categoria na pergunta. Tente mencionar a categoria exata."}
    
    with get_session() as session:
        total = session.scalar(
            select(func.sum(Transaction.amount))
            .where(func.lower(Transaction.category) == matched_category)
        )

    total_spent = total if total is not None else 0.0

    return {
        "answer": f"Você gastou R${total_spent:.2f} em {matched_category}."
    }

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    message = data.get("message")

    prompt = f"""
    Extraia os dados financeiros da frase: "{message}"

    Responda **apenas** com um JSON válido como no exemplo abaixo (sem explicações):

    {{
        "amount": 123.45,
        "category": "Alimentação",
        "date": "2025-07-09"
    }}

    Não use blocos de código, markdown ou aspas. Retorne apenas o JSON puro.
    """

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    content = response.choices[0].message.content.strip()

    try:
        parsed = json.loads(content)

        amount = float(parsed["amount"])
        category = parsed["category"]

        if parsed.get("date"):
            date = datetime.fromisoformat(parsed["date"])
        else:
            date = datetime.now()

        with get_session() as session:
            transaction = Transaction(
                message=message,
                amount=amount,
                category=category,
                date=date
            )

            session.add(transaction)
            session.commit()

        return {
            "reply": f"Registrado! 💸 R${amount:.2f} em {category} ({date.date()})"
        }
    
    except Exception as e:
        return {
            "error": "Erro ao processar transação",
            "details": str(e),
            "raw_content": content
        }
