import os
from pathlib import Path
from typing import Optional
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from src.config import DATA_DIR


@tool
def read_sample_portfolio(json_path: Optional[str] = None) -> str:
    """Reads the sample_portfolio.json file and returns a human-readable string."""
    path = Path(json_path) if json_path else (DATA_DIR / "sample_portfolio.json")
    if not path.exists():
        return f"File not found: {path}"

    import json
    with path.open("r", encoding="utf-8") as f:
        portfolio = json.load(f)

    if not isinstance(portfolio, list):
        return "Unexpected portfolio format."

    response_lines = ["Sample Portfolio:"]
    for stock in portfolio:
        response_lines.append(
            f"- {stock['symbol']} ({stock['sector']}): {stock['quantity']} shares @ ${stock['purchase_price']} (Bought on {stock['purchase_date']})"
        )
    return "\n".join(response_lines)