from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(
    model_name="gpt-4",   # or "gpt-3.5-turbo"
    temperature=0.7
)