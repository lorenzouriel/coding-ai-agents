from langchain.chat_models import ChatOllama
from crewai import CrewSettings

llm = ChatOllama(
    model="mistral",  # ou "llama3", "phi3", etc
    temperature=0.7
)

CrewSettings.llm = llm