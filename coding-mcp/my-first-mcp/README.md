## Install Deps
```bash
uv add fastmcp mcp[cli] "huggingface_hub[mcp]>=0.32.0"
```

## Login to HF
```bash
huggingface-cli login
```

## Run Playwright
```bash
tiny-agents run agent.json
```