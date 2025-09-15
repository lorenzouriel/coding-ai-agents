import os
import json
from pathlib import Path
from dotenv import load_dotenv

# --- Load environment variables ---
ENV_PATH = Path(__file__) / ".env"
load_dotenv(dotenv_path=ENV_PATH, override=True)

# --- Add src to Python path ---
import sys
SRC_DIR = Path(__file__) / "src"
sys.path.insert(0, str(SRC_DIR))

# --- Imports from src ---
from src.config import DATA_DIR
from src.agents.portfolio_reader import generate_portfolio
from src.agents.research import search_node, State
from src.agents.portfolio_reader import read_portfolio_node
from src.agents.report_writer import doc_writing_node
from src.agents.supervisor import make_supervisor_node
from langchain.chat_models import ChatOpenAI
from langgraph.graph import StateGraph, START

# --- Step 1: Initialize OpenAI LLM ---
llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)

# --- Step 2: Generate sample portfolio ---
portfolio = generate_portfolio()
portfolio_file = DATA_DIR / "sample_portfolio.json"
portfolio_file.parent.mkdir(parents=True, exist_ok=True)
with open(portfolio_file, "w") as f:
    json.dump(portfolio, f, indent=4)
print(f"✅ Portfolio JSON saved to '{portfolio_file}'")

# --- Step 3: Setup supervisor ---
supervisor_node = make_supervisor_node(llm, ["search", "read_portfolio", "doc_writer"])

# --- Step 4: Build state graph ---
builder = StateGraph(State)
builder.add_node("supervisor", supervisor_node)
builder.add_node("search", search_node)
builder.add_node("read_portfolio", read_portfolio_node)
builder.add_node("doc_writer", doc_writing_node)
builder.add_edge(START, "supervisor")
super_graph = builder.compile()

# --- Step 5: Run the multi-agent pipeline ---
initial_state = {
    "messages": [
        ("user", "Generate a well-structured report on how to improve my portfolio given the market landscape in Q4 2025.")
    ]
}

print("\n=== Running Multi-Agent Graph ===\n")
for state in super_graph.stream(initial_state, {"recursion_limit": 150}):
    print(state)
    print("---")

print("\n✅ Multi-agent pipeline finished.")
