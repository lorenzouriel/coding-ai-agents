from mcp.server.fastmcp import FastMCP
import yfinance as yf
from typing import List, Dict

# Create an MCP server
mcp = FastMCP("FinanceDemo")

# -------------------------
# TOOLS
# -------------------------

@mcp.tool()
def get_stock_price(ticker: str) -> float:
    """
    Fetch the latest stock price for a given ticker symbol from Yahoo Finance.
    
    Args:
        ticker (str): Stock ticker symbol, e.g. 'AAPL'
    Returns:
        float: Latest closing stock price
    """
    stock = yf.Ticker(ticker)
    return stock.history(period="1d")["Close"].iloc[-1]


@mcp.tool()
def get_company_info(ticker: str) -> Dict[str, str]:
    """
    Fetch basic company information (name, sector, industry).
    
    Args:
        ticker (str): Stock ticker symbol
    Returns:
        dict: Company info
    """
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        "longName": info.get("longName", "N/A"),
        "sector": info.get("sector", "N/A"),
        "industry": info.get("industry", "N/A"),
        "website": info.get("website", "N/A"),
    }


@mcp.tool()
def get_historical_prices(ticker: str, period: str = "5d") -> List[float]:
    """
    Fetch historical closing prices for a stock.
    
    Args:
        ticker (str): Stock ticker symbol
        period (str): Time period (e.g., '5d', '1mo', '3mo', '1y')
    Returns:
        list: List of closing prices
    """
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    return hist["Close"].round(2).tolist()


@mcp.tool()
def get_top_holders(ticker: str) -> List[Dict[str, str]]:
    """
    Fetch the top institutional holders of the company.
    
    Args:
        ticker (str): Stock ticker symbol
    Returns:
        list of dict: Each holder with 'holder' and 'shares'
    """
    stock = yf.Ticker(ticker)
    holders = stock.institutional_holders
    if holders is None:
        return []
    return holders[["Holder", "Shares"]].head(5).to_dict(orient="records")


@mcp.tool()
def get_price_summary(ticker: str, period: str = "1mo") -> Dict[str, float]:
    """
    Get summary statistics (min, max, avg) for a given period.
    
    Args:
        ticker (str): Stock ticker symbol
        period (str): Time period (e.g., '1mo', '3mo', '6mo')
    Returns:
        dict: Summary with min, max, and avg closing prices
    """
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    prices = hist["Close"]
    return {
        "min": float(prices.min()),
        "max": float(prices.max()),
        "avg": float(prices.mean().round(2))
    }

# -------------------------
# MAIN
# -------------------------

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
