from crewai import Agent, Task, Crew
from crewai_tools import MCPServerAdapter
import os

# Configure MCP server connection
server_params = {
    "url": "http://localhost:8080/mcp",
    "transport": "streamable-http"
}


# Connect to MCP server and get tools
with MCPServerAdapter(server_params, connect_timeout=60) as mcp_tools:
    # Create a database analyst agent
    db_analyst = Agent(
        role="Database Analyst",
        goal="Analyze SQL Server database and provide insights",
        backstory="You are an expert database analyst who can query databases, "
                 "explore schemas, and extract meaningful insights from data.",
        tools=mcp_tools,  # All MCP tools are automatically available
        verbose=True
    )

    # Create an analysis task
    analysis_task = Task(
        description="""
        Perform a comprehensive database analysis:
        1. Check if the database connection is healthy
        2. List all available schemas
        3. For the 'dbo' schema, list all tables
        4. Get information about the database server
        5. Provide a summary of your findings
        """,
        expected_output="A detailed report of the database structure",
        agent=db_analyst
    )

    # Create and run the crew
    crew = Crew(
        agents=[db_analyst],
        tasks=[analysis_task],
        verbose=True
    )

    # Execute the analysis
    result = crew.kickoff()
    print(result)