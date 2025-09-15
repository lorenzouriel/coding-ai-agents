"""Generates a sample portfolio JSON."""
from datetime import datetime
import json
import random
from pathlib import Path
from typing import List
from src.config import DATA_DIR

SAMPLE_ASSETS = [
    {"symbol": "AAPL", "sector": "Technology"},
    {"symbol": "GOOGL", "sector": "Technology"},
    {"symbol": "MSFT", "sector": "Technology"},
    {"symbol": "AMZN", "sector": "Consumer Discretionary"},
    {"symbol": "TSLA", "sector": "Consumer Discretionary"},
    {"symbol": "JNJ", "sector": "Healthcare"},
    {"symbol": "NVDA", "sector": "Technology"},
    {"symbol": "XOM", "sector": "Energy"},
]


def generate_portfolio(assets: List[dict], out_path: Path = DATA_DIR / "sample_portfolio.json") -> Path:
    portfolio = []
    for asset in assets:
        quantity = random.randint(5, 100)
        purchase_price = round(random.uniform(50, 3000), 2)
        total_invested = round(quantity * purchase_price, 2)
        purchase_date = datetime.strftime(datetime(2022, random.randint(1, 12), random.randint(1, 28)), "%Y-%m-%d")

        portfolio.append({
            "symbol": asset["symbol"],
            "sector": asset.get("sector", "Unknown"),
            "quantity": quantity,
            "purchase_price": purchase_price,
            "total_invested": total_invested,
            "purchase_date": purchase_date,
        })

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(portfolio, f, indent=2)
    return out_path


if __name__ == "__main__":
    path = generate_portfolio(SAMPLE_ASSETS)
    print(f"Generated portfolio at: {path}")