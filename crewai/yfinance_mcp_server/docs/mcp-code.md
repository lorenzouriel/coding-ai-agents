## Imports

```python
from dotenv import load_dotenv
```

* Loads environment variables from a `.env` file.

```python
from fastmcp import FastMCP
```

* Used to set up a multi-agent command protocol server (`FastMCP`).

```python
from langchain_openai import ChatOpenAI
```

* Loads OpenAI chat models (here using `gpt-4.1-mini`) through LangChain.

```python
from crewai import Agent, Task, Crew, Process
```

* Core components of CrewAI:

  * `Agent`: Defines a role with tools, memory, and behavior.
  * `Task`: Defines a job the agent needs to complete.
  * `Crew`: Groups agents and tasks together in a workflow.
  * `Process`: Determines how tasks are processed (sequentially here).

```python
from crewai.memory import EntityMemory
from crewai.memory.storage.rag_storage import RAGStorage
```

* Used to manage per-user short-term memory with RAG (Retrieval Augmented Generation) storage.

```python
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters
```

* `MCPServerAdapter` connects external tools (like Supabase or YFinance) via command-line processes.

```python
import os
```

* Accesses system environment variables.

## Initialization

```python
load_dotenv()
mcp = FastMCP("multi-agent-server")
```

* Loads environment and initializes a FastMCP server named `"multi-agent-server"`.

## User Memory Handler

```python
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
```

* Initializes **short-term memory** for a user using RAG + OpenAI embedding.
* Each user gets a unique memory path.

## Tool Definition - `multi_analyst_tool`

```python
@mcp.tool(name="multi_analyst")
async def multi_analyst_tool(question: str, user_id: str) -> str:
```

* Defines an **async tool** registered to FastMCP that:
  * Receives a question and user ID.
  * Handles financial and database questions.

### Tool Parameters

```python
yfinance_params = StdioServerParameters(command="uvx", args=["yfmcp@latest"])
```

* Runs a tool (like YFinance) via command line (`uvx yfmcp@latest`).

```python
supabase_params = StdioServerParameters(
    command="npx",
    args=["-y", "@supabase/mcp-server-supabase@latest"],
    env={"SUPABASE_ACCESS_TOKEN": os.getenv("SUPABASE_ACCESS_TOKEN"), **os.environ},
)
```

* Runs the Supabase MCP adapter using `npx`.

### Adapter Setup

```python
yfinance_adapter = MCPServerAdapter(yfinance_params)
supabase_adapter = MCPServerAdapter(supabase_params)
```

* Initializes adapters for the two tools.
* Gathers their capabilities into `tools = ... + ...`.

### Agent Configuration

```python
multi_analyst = Agent(
    role="Professional Data & Finance Analyst",
    goal="Answer any financial or database question...",
    backstory="Expert in SQL, stocks, KPIs...",
    tools=tools,
    llm=llm,
    allow_delegation=False,
    memory=memory,
)
```

* Defines the AI agent responsible for answering the query using provided tools and memory.

### Task Setup

```python
task = Task(
    description=f"Handle this user question: {question}",
    expected_output="Useful response using the most suitable tool.",
    ...
)
```

* Describes what the agent should do.

### Crew Assembly

```python
crew = Crew(
    agents=[multi_analyst],
    tasks=[task],
    process=Process.sequential,
    memory=True,
    entity_memory=memory,
    verbose=True,
)
```

* Creates a team (`Crew`) of agents and tasks.
* Runs in **sequential mode** using **entity memory**.

### Execution

```python
result = await crew.kickoff_async()
return result
```

* Kicks off the task asynchronously and returns the result.

### Cleanup
```python
finally:
    for adapter in mcp_adapters:
        try:
            adapter.stop()
```

* Stops each adapter process (cleans up resources).

## Server Execution
```python
if __name__ == "__main__":
    mcp.run(transport="sse", host="127.0.0.1", port=8005)
```

* Runs the MCP server using **SSE (Server-Sent Events)** on localhost port `8005`.

## Summary
This code:
* Sets up a **FastMCP server**.
* Defines a tool `multi_analyst` that spins up agents to:
  * Analyze financial/DB queries.
  * Use external tools via MCP (YFinance and Supabase).
  * Use per-user short-term memory with LangChain embeddings.
* Runs everything in a modular, async, and scalable way.

Would you like a diagram of how the components interact?