from dotenv import load_dotenv
from fastmcp import FastMCP
from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew, Process
from crewai.memory import EntityMemory
from crewai.memory.storage.rag_storage import RAGStorage
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters
import os

load_dotenv()
mcp = FastMCP("multi-agent-server")

def get_user_memory(user_id: str):
    return EntityMemory(
        storage=RAGStorage(
            embedder_config={
                "provider": "openai",
                "config": {"model": "text-embedding-3-small"},
            },
            type="short_term",
            path=f"./memory_store/{user_id}/",
        )
    )

@mcp.tool(name="multi_analyst")
async def multi_analyst_tool(question: str, user_id: str) -> str:
    """Handle airbnb and DB questions using unified tool access."""
    airbnb_params = StdioServerParameters(command="npx", args=["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"])

    mcp_adapters = []
    try:
        airbnb_adapter = MCPServerAdapter(airbnb_params)
        mcp_adapters = [airbnb_adapter]

        tools = airbnb_adapter.tools
        llm = ChatOpenAI(model="gpt-4.1-mini")
        memory = get_user_memory(user_id)

        multi_analyst = Agent(
            role="Professional Renting & Vacation Rental Analyst",
            goal="Answer any question using airbnb and Supabase tools.",
            backstory="Expert in SQL, renting, KPIs, and databases. Decides the best tool for each query.",
            tools=tools,
            verbose=True,
            llm=llm,
            allow_delegation=False,
            memory=memory,
        )

        task = Task(
            description=f"Handle this user question: {question}",
            expected_output="Useful response using the most suitable tool.",
            tools=tools,
            agent=multi_analyst,
            memory=memory,
        )

        crew = Crew(
            agents=[multi_analyst],
            tasks=[task],
            process=Process.sequential,
            memory=True,
            entity_memory=memory,
            verbose=True,
        )

        result = await crew.kickoff_async()
        return result
    finally:
        for adapter in mcp_adapters:
            try:
                adapter.stop()
            except Exception:
                pass


if __name__ == "__main__":
    mcp.run(transport="sse", host="127.0.0.1", port=8005)