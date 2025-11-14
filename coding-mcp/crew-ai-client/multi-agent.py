from crewai import Agent, Task, Crew, Process
from crewai_tools import MCPServerAdapter
import os

server_params = {"url": "http://localhost:8080/mcp", "transport": "streamable-http"}

with MCPServerAdapter(server_params) as mcp_tools:
    # Schema Explorer Agent
    explorer = Agent(
        role="Schema Explorer",
        goal="Discover and document database structure",
        tools=mcp_tools,
        verbose=True
    )

    # Data Analyst Agent
    analyst = Agent(
        role="Data Analyst",
        goal="Analyze data patterns and find insights",
        tools=mcp_tools,
        verbose=True
    )

    # Tasks
    explore_task = Task(
        description="Explore the database schema and list all tables",
        agent=explorer
    )

    analyze_task = Task(
        description="Based on discovered tables, find top 10 most important records",
        agent=analyst,
        context=[explore_task]  # Depends on explore_task
    )

    crew = Crew(
        agents=[explorer, analyst],
        tasks=[explore_task, analyze_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    print(result)