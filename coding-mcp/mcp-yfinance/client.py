import asyncio
import json
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    """
    Main function to interact with the finance demo server.
    """
    try:
        # Use sys.executable to ensure the correct Python interpreter from the
        # virtual environment is used to run the server as a subprocess.
        print("Starting server subprocess with sys.executable...")
        async with stdio_client(StdioServerParameters(command=sys.executable, args=["server.py"])) as (
            reader,
            writer,
        ):
            # The ClientSession manages the communication and tool calls.
            async with ClientSession(reader, writer) as client:
                print("Connection to server successful. Listing tools...")
                try:
                    tools = await client.list_tools()
                    print(f"Available tools: {', '.join([t.name for t in tools])}\n")

                    # Example 1: Get the latest stock price for AAPL
                    print("--- Fetching AAPL stock price ---")
                    # The await keyword is necessary because tool calls are asynchronous.
                    price = await client.get_stock_price(ticker="AAPL")
                    print(f"Current price of AAPL: ${price:.2f}\n")

                    # Example 2: Get company information for GOOG
                    print("--- Fetching GOOG company info ---")
                    info = await client.get_company_info(ticker="GOOG")
                    print(f"Google (GOOG) Info:\n{json.dumps(info, indent=2)}\n")

                    # Example 3: Get historical prices for TSLA over the last 5 days
                    print("--- Fetching TSLA historical prices (5d) ---")
                    historical_prices = await client.get_historical_prices(ticker="TSLA", period="5d")
                    print(f"Tesla (TSLA) prices for the last 5 days: {historical_prices}\n")

                    # Example 4: Get top institutional holders for MSFT
                    print("--- Fetching top MSFT holders ---")
                    top_holders = await client.get_top_holders(ticker="MSFT")
                    if top_holders:
                        print(f"Top 5 institutional holders for Microsoft (MSFT):\n{json.dumps(top_holders, indent=2)}\n")
                    else:
                        print("No institutional holders found for MSFT.\n")

                    # Example 5: Get price summary for AMZN over the last month
                    print("--- Fetching AMZN price summary (1mo) ---")
                    summary = await client.get_price_summary(ticker="AMZN", period="1mo")
                    print(f"Amazon (AMZN) 1-month price summary:\n{json.dumps(summary, indent=2)}\n")

                except Exception as tool_e:
                    # This error indicates the server is not responding to a valid tool call.
                    # It most likely means the server process itself failed to initialize its tools.
                    print(f"An error occurred during tool execution: {tool_e}")
                    print("This is likely a server-side issue. Please verify the `server.py` file and its dependencies.")

    except Exception as e:
        # This error indicates a failure to even connect to the server process.
        print(f"An error occurred during server connection or startup: {e}")
        print("This often means the server process failed to start. Please ensure `yfinance` and `FastMCP` are correctly installed.")


if __name__ == "__main__":
    asyncio.run(main())
