from langchain_community.tools.tavily_search import TavilySearchResults
from src.config import TAVILY_API_KEY

def create_tavily_tool(max_results: int = 5):
    if not TAVILY_API_KEY:
        raise RuntimeError("TAVILY_API_KEY is not set in environment")
    return TavilySearchResults(max_results=max_results, tavily_api_key=TAVILY_API_KEY)