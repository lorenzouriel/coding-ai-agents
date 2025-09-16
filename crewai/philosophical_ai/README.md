# Philosophical Agents Crew
A Python project demonstrating multi-agent philosophical reasoning using **CrewAI**. Each agent represents a distinct philosophical perspective, contributing to discussions on ethical questions. The system allows synthesis of diverse viewpoints into a coherent, reflective answer.

## Features
* **Philosophical Agents:**
  Each agent embodies a philosophical school of thought:
  * **Stoic Philosopher:** Focus on virtue, reason, and acceptance of fate.
  * **Nihilist Thinker:** Challenges claims of inherent meaning or objective truth.
  * **Existential Philosopher:** Emphasizes human freedom, responsibility, and self-created meaning.
  * **Utilitarian Analyst:** Evaluates ethical questions to maximize collective happiness.
  * **Buddhist Philosopher:** Offers guidance rooted in mindfulness, non-attachment, and reduction of suffering.
  * **Socratic Critic:** Interrogates assumptions, exposing weaknesses in arguments.
  * **Philosophical Moderator:** Synthesizes perspectives into a well-rounded answer.
* **Task-Oriented Reasoning:**
  Each agent performs specific tasks, generating perspectives or critical analysis on ethical questions.
* **CrewAI Integration:**
  Agents are coordinated in a **Crew** for collaborative reasoning and final synthesis.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/lorenzouriel/coding-ai-agents.git
cd coding-ai-agents/crewai/philosophical_ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key into `.env`:
```bash
OPENAI_API_KEY=
```

## Usage
Run the main script:
```bash
python main.py
```

This will:
1. Pose a philosophical question to the agents.
2. Collect each agent’s perspective.
3. Use the Socratic agent to critically examine arguments.
4. Have the moderator synthesize a final multi-perspective answer.

Example output snippet:
```
🧠 Final Answer:
[Moderator's synthesized philosophical analysis of the ethical question]
```

## Example Question
```python
question = "Is it ethical to use AI in healthcare decisions, such as diagnosis or treatment?"
```

Each agent responds according to their philosophical stance, and the final answer is a balanced reflection of all perspectives.

## Project Structure
```bash
philosophical-agents-crew/
├─ main.py            # Core script defining agents, tasks, and crew
├─ README.md          # This file
└─ requirements.txt   # Python dependencies
```