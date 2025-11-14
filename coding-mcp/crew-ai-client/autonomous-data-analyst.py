from crewai import Agent, Task, Crew
from crewai_tools import MCPServerAdapter

server = {"url": "http://localhost:8080/mcp", "transport": "streamable-http"}

with MCPServerAdapter(server) as tools:
    sql_analyst = Agent(
        role="Database Analyst",
        goal="Query the database and extract raw insights.",
        backstory=(
            "You are an expert SQL analyst with deep experience working with MCP tools. "
            "You focus on extracting clean, structured datasets with zero commentary."
        ),
        tools=tools,
        verbose=True,
    )

    viz_analyst = Agent(
        role="Visualization Expert",
        goal="Transform insights into visual summaries and business insights.",
        backstory=(
            "You specialize in interpreting numerical data, identifying trends, and "
            "producing business-relevant insights and visualization structures."
        ),
        verbose=True,
    )

    task_extract = Task(
        description=(
            "Query the database for investments by month for the last 12 months. "
            "Return only clean, structured tabular data."
        ),
        expected_output=(
            "A clean structured dataset with the following columns:\n"
            "- month (YYYY-MM)\n"
            "- total_sales (numeric)\n"
            "Returned as pure text or JSON, no commentary."
        ),
        agent=sql_analyst
    )

    task_visualize = Task(
        description=(
            "Take the structured data from the SQL analyst and generate:\n"
            "1. A written business analysis\n"
            "2. 2–3 strategic recommendations\n"
            "3. A chart-ready data description (NO images, just structure)."
        ),
        expected_output=(
            "A fully structured response containing:\n"
            "- Business Analysis: A narrative of the last 12 months trends\n"
            "- Recommendations: 2–3 bullet points\n"
            "- Chart Data Description: JSON-like structure describing axes, labels, and data"
        ),
        agent=viz_analyst
    )

    crew = Crew(
        agents=[sql_analyst, viz_analyst],
        tasks=[task_extract, task_visualize],
        verbose=True
    )

    print(crew.kickoff())
