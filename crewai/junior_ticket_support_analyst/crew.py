from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from crewai.knowledge.source.crew_docling_source import CrewDoclingSource

# PDF knowledge source
pdf_tool = PDFKnowledgeSource(
    file_paths=["system_manual.pdf", "culture_code.pdf"]
)

# Markdown knowledge source
md_tool = TextFileKnowledgeSource(
    file_paths=["setup_guide.md", "troubleshooting.md", "feature_faq.md"]
)

llm = LLM(model="gpt-4o-mini", temperature=0)

@CrewBase
class JuniorSupportCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def junior_ticket_support_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["junior_ticket_support_agent"],
            verbose=True,
            llm=llm,
            # knowledge_sources=[pdf_tool, md_tool],  # Both types of documents
        )

    @task
    def answer_system_faq(self) -> Task:
        return Task(
            config=self.tasks_config["answer_system_faq"],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.junior_ticket_support_agent()],
            tasks=[self.answer_system_faq()],
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[pdf_tool, md_tool],  # Both types of documents
        )