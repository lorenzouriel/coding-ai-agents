from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

pdf_tool = PDFKnowledgeSource(
    file_paths=["politica-protecao-de-dados.pdf", "politica-de-privacidade.pdf"]
)

# llm = LLM(model="groq/llama-3.3-70b-versatile", temperature=0)
llm = LLM(model="gpt-4o-mini", temperature=0)

@CrewBase
class SpecialistCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def specialist_lgpd(self) -> Agent:
        return Agent(
            config=self.agents_config["specialist_lgpd"],
            verbose=True,
            llm=llm,
            # knowledge_sources=[pdf_tool],
        )
    
    @task
    def answers_lgpd_question(self) -> Task:
        return Task(
            config=self.tasks_config["answers_lgpd_question"],
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.specialist_lgpd()],
            tasks=[self.answers_lgpd_question()],
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[pdf_tool],
        )