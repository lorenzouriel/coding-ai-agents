from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from textwrap import dedent

load_dotenv()

# Initialize Groq LLM wrapper
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="deepseek-r1-distill-llama-70b"
)

# Define one agent as example
stoic_agent = Agent(
    role="Stoic Philosopher",
    goal="Provide wisdom grounded in Stoicism",
    backstory="Disciple of Marcus Aurelius, values virtue and reason",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Define one task
question = "Is it ethical to use AI in healthcare decisions, such as diagnosis or treatment?"

task_stoic = Task(
    description=f"Give a Stoic perspective on the question: '{question}'",
    expected_output="A Stoic ethical analysis focusing on virtue and reason.",
    agent=stoic_agent
)

# Create Crew
philosophy_crew = Crew(
    agents=[stoic_agent],
    tasks=[task_stoic],
    verbose=True
)

if __name__ == "__main__":
    result = philosophy_crew.kickoff()
    print("\n🧠 Final Answer:\n")
    print(result)