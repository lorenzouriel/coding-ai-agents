from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)

OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
USER_AGENT = os.getenv("USER_AGENT", "multi-agent-app/1.0")

OUTPUTS_DIR = BASE_DIR / "outputs"
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)