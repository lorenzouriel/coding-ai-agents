## Imports
```python
import streamlit as st
import asyncio
from fastmcp import Client
import json
import pandas as pd
import uuid
import nest_asyncio
```

* `streamlit`: Used to build the web UI.
* `asyncio`: For async operations (calling the AI agent).
* `fastmcp.Client`: Allows client-side interaction with the MCP tool server.
* `json`: For parsing/handling JSON responses.
* `pandas`: Used to display tabular data.
* `uuid`: Used to assign a unique ID to the user.
* `nest_asyncio`: Allows nested use of `asyncio.run()` inside Streamlit.

```python
nest_asyncio.apply()
```

* Makes the event loop re-entrant so Streamlit can run async code (required when using `asyncio` in notebooks or Streamlit apps).

## Streamlit Page Setup
```python
st.set_page_config(page_title="Multi-Agent Analyst Chat", page_icon="🤖", layout="wide")
st.title("Multi-Agent Analyst – AI Chat Interface")
```

* Sets up the Streamlit page configuration (title, emoji icon, wide layout).

## Session State Initialization
```python
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []
```

* Assigns a **unique user ID** for memory scoping (used in the backend memory RAG path).
* Initializes an in-memory chat history.

## Show Chat History
```python
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
```

* Displays all previous messages from the user and assistant in the UI.

## Async MCP Agent Call
```python
async def call_agent(question: str, user_id: str):
    client = Client("http://127.0.0.1:8005/sse")
    async with client:
        result = await client.call_tool(
            "multi_analyst", {"question": question, "user_id": user_id}
        )
        return result[0].text if result and hasattr(result[0], "text") else str(result)
```

* Creates a connection to the **FastMCP SSE server**.
* Calls the registered tool `multi_analyst` with the question and user ID.
* Returns the `text` response (if present) or stringifies the full response.

## Handle New User Input
```python
if prompt := st.chat_input("Ask me anything ..."):
```

* Waits for user input in the chat bar.

### Log User Input
```python
st.session_state.messages.append({"role": "user", "content": prompt})
```

* Stores the user message in the session history.

### Call Agent & Render Response
```python
with st.chat_message("assistant"):
    with st.spinner("The agent is thinking..."):
        try:
            response = asyncio.run(call_agent(prompt, st.session_state.user_id))
```

* Shows a spinner while the agent processes the request.
* Calls the agent asynchronously using `asyncio.run`.

### Parse & Display Response
```python
try:
    resp_json = json.loads(response)
    ...
except Exception:
    display_data = response
```

* Tries to parse the response as JSON.
* If structured like:

  ```json
  {
    "tasks_output": [{"raw": [...] }]
  }
  ```

  it extracts the `"raw"` content as `display_data`.

### Show Result as Table or JSON
```python
try:
    data = json.loads(display_data)
    if isinstance(data, list) and all(isinstance(row, dict) for row in data):
        df = pd.DataFrame(data)
        st.dataframe(df)
        response = None
    else:
        st.json(data)
        response = None
except Exception:
    response = display_data
```

* Attempts to show `display_data` as:

  * `DataFrame` if it’s a list of dictionaries.
  * Pretty JSON if it’s a dict.
  * Fallback: raw string if parsing fails.

### Handle Errors Gracefully
```python
except Exception as e:
    import traceback
    tb = traceback.format_exc()
    response = f"Error: {e}\n\nTraceback:\n{tb}"
```

* Catches and displays any unexpected errors (useful for debugging during dev).

## Save Assistant Response
```python
st.session_state.messages.append({
    "role": "assistant",
    "content": response if response else "[Structured output above]",
})
```

* Saves the assistant's response to the message history for persistence.

## Summary
| Component                 | Description                                                             |
| ------------------------- | ----------------------------------------------------------------------- |
| **`FastMCP`**             | Backend server that runs agents/tools.                                  |
| **Streamlit App**         | Frontend UI that sends questions to the backend and displays responses. |
| **UUID Session**          | Keeps chat memory scoped per user.                                      |
| **Async Agent Call**      | Uses `asyncio` to call the agent over FastMCP.                          |
| **Data Display Logic**    | Tries to parse and display structured data smartly.                     |
| **Stateful Chat History** | Remembers full conversation for continuity.                             |
