## **Option 1 — Using `run.py` (Recommended)**
1. Make sure `run.py` is in the **project root** (`financial_multi_agent_app/`) as we created before.
2. Ensure your `.env` has **all keys**, e.g., OpenAI:
```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_key
ALPHAVANTAGE_API_KEY=your_alphavantage_key
USER_AGENT=multi-agent-app/1.0
```

3. From the **project root**, run:
```powershell
python run.py
```

This will:
* Generate `sample_portfolio.json`.
* Run the **research agent**.
* Run the **portfolio reader agent**.
* Run the **report generator agent**.
* Save the final report automatically.

## **Option 2 — Without `run.py` (Module Approach)**
You can run each agent individually from the **project root** using Python modules.

1. Make sure `src` is a package:
```bash
src/__init__.py
src/agents/__init__.py
```

2. From **project root**:
```powershell
# Run the research agent
python -m src.agents.research

# Run the portfolio reader agent
python -m src.agents.portfolio_reader

# Run the report writer agent
python -m src.agents.report_writer
```

* Inside each script, use **absolute imports**:
```python
from src.config import DATA_DIR
from src.agents.portfolio_reader import read_portfolio_node
from src.agents.report_writer import doc_writing_node
```

* Python will correctly resolve `src` because you are running from the **root**.
