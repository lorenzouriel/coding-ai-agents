from crewai import Agent, Task, Crew
from textwrap import dedent
from llm import openai_llm

# ----------------------
# Philosophical Agents
# ----------------------

stoic_agent = Agent(
    role="Stoic Philosopher",
    goal="Provide wisdom grounded in Stoicism, focusing on virtue and reason",
    backstory="A disciple of Marcus Aurelius and Epictetus, values rationality and inner peace",
    verbose=True,
    allow_delegation=False,
    llm=openai_llm
)

nihilist_agent = Agent(
    role="Nihilist Thinker",
    goal="Challenge all claims of inherent meaning or objective truth",
    backstory="An intellectual follower of Nietzsche and Cioran, skeptical and contrarian by nature",
    verbose=True,
    allow_delegation=False,
    llm=openai_llm 
)

existential_agent = Agent(
    role="Existential Philosopher",
    goal="Explore human freedom, responsibility, and subjective meaning",
    backstory="Inspired by Sartre and Camus, this thinker sees meaning as self-made",
    verbose=True,
    allow_delegation=False,
    llm=openai_llm 
)

utilitarian_agent = Agent(
    role="Utilitarian Analyst",
    goal="Evaluate ethical questions by maximizing collective happiness",
    backstory="Rooted in the philosophies of Bentham and Mill, values outcomes and logic",
    verbose=True,
    allow_delegation=False,
    llm=openai_llm 
)

buddhist_agent = Agent(
    role="Buddhist Philosopher",
    goal="Offer a perspective rooted in mindfulness, non-attachment, and the reduction of suffering (dukkha)",
    backstory="A contemplative mind shaped by teachings of the Buddha, focused on the Middle Way and right action",
    verbose=True,
    allow_delegation=False,
    llm=openai_llm 
)

socratic_agent = Agent(
    role="Socratic Critic",
    goal="Critically examine the assumptions of all philosophical arguments to seek clearer truth",
    backstory="A relentless interrogator in the style of Socrates, always asking 'What do you mean by that?' and 'Why?'",
    verbose=True,
    allow_delegation=False,
    llm=openai_llm 
)

# ----------------------
# Moderator Agent
# ----------------------

moderator_agent = Agent(
    role="Philosophical Moderator",
    goal="Synthesize a well-rounded philosophical answer by guiding discussion",
    backstory="An impartial thinker who values all perspectives and seeks synthesis",
    verbose=True,
    allow_delegation=False,
    llm=openai_llm 
)

# ----------------------
# Define Tasks
# ----------------------

question = "Is it ethical to use AI in healthcare decisions, such as diagnosis or treatment?"

task_moderate = Task(
    description=dedent(f"""
        Present the question: '{question}' to the other philosophers.
        Let them give their perspectives, and synthesize their arguments into a thoughtful final answer.
    """),
    expected_output="A final multi-perspective ethical analysis of the question, highlighting agreement and disagreement.",
    agent=moderator_agent
)

task_socratic = Task(
    description=dedent(f"""
        Read the responses from the Stoic, Nihilist, Existentialist, and Utilitarian agents on the question:
        '{question}'.

        Critically examine each of their positions by asking probing questions that reveal assumptions,
        contradictions, or lack of clarity. Do not offer your own conclusions — just expose weaknesses and ambiguities.
    """),
    expected_output="A list of critical questions and challenges for each philosopher's position, organized by agent.",
    agent=socratic_agent
)

task_stoic = Task(
    description=f"Give a Stoic perspective on the question: '{question}'",
    expected_output="A Stoic analysis focusing on duty, virtue, and acceptance of fate.",
    agent=stoic_agent
)

task_nihilist = Task(
    description=f"Give a Nihilist perspective on the question: '{question}'",
    expected_output="A Nihilist critique emphasizing meaninglessness or ethical illusion.",
    agent=nihilist_agent
)

task_existential = Task(
    description=f"Give an Existentialist perspective on the question: '{question}'",
    expected_output="An Existentialist view focusing on individual choice, freedom, and authenticity.",
    agent=existential_agent
)

task_utilitarian = Task(
    description=f"Give a Utilitarian analysis on the question: '{question}'",
    expected_output="A cost-benefit based view focused on collective well-being.",
    agent=utilitarian_agent
)

task_buddhist = Task(
    description=f"Give a Buddhist philosophical response to the question: '{question}'",
    expected_output="A response grounded in the Four Noble Truths, mindfulness, compassion, and impermanence.",
    agent=buddhist_agent
)

# ----------------------
# Create Crew and Run
# ----------------------

philosophy_crew = Crew(
    agents=[
        moderator_agent,
        stoic_agent,
        nihilist_agent,
        existential_agent,
        utilitarian_agent,
        buddhist_agent,
        socratic_agent
    ],
    tasks=[
        task_stoic,
        task_nihilist,
        task_existential,
        task_utilitarian,
        task_buddhist,
        task_socratic,
        task_moderate
    ],
    verbose=True
)

if __name__ == "__main__":
    result = philosophy_crew.kickoff()
    print("\n🧠 Final Answer:\n")
    print(result)
