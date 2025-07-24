## Installation
First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:
```bash
crewai install
```

### Customizing
**Add your `OPENAI_API_KEY` into the `.env` file**
- Modify `src/guide_creator_flow/config/agents.yaml` to define your agents
- Modify `src/guide_creator_flow/config/tasks.yaml` to define your tasks
- Modify `src/guide_creator_flow/crew.py` to add your own logic, tools and specific args
- Modify `src/guide_creator_flow/main.py` to add custom inputs for your agents and tasks

## Running the Project
To kickstart your flow and begin execution, run this from the root folder of your project:
```bash
crewai flow kickoff
```

When you run this command, you’ll see your flow spring to life:
1. It will prompt you for a topic and audience level
2. It will create a structured outline for your guide
3. It will process each section, with the content writer and reviewer collaborating on each
4. Finally, it will compile everything into a comprehensive guide

## Visualize Your Flow
One of the powerful features of flows is the ability to visualize their structure:
```bash
crewai flow plot
```
- This will create an HTML file that shows the structure of your flow, including the relationships between different steps and the data that flows between them. This visualization can be invaluable for understanding and debugging complex flows.

## Review the Output
Once the flow completes, you’ll find two files in the output directory:
- `guide_outline.json`: Contains the structured outline of the guide
- `complete_guide.md`: The comprehensive guide with all sections