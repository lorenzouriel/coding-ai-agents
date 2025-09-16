from langchain_community.chat_models import ChatOllama, ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI LLM
openai_key = os.getenv("OPENAI_API_KEY")

openai_llm = ChatOpenAI(
    model_name="gpt-4",
    temperature=0.7,
    openai_api_key=openai_key
)

# Optionally initialize Ollama LLM
# ollama_llm = ChatOllama(
#     model="mistral",
#     temperature=0.7
# )
# CrewSettings.llm = ollama_llm

# groq_key = os.getenv("GROQ_API_KEY")
# groq_llm = ChatGroq(api_key=groq_key, model="deepseek-r1-distill-llama-70b")
# CrewSettings.llm = groq_llm