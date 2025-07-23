# Specialist Crew - LGPD Assistant
This project uses the [CrewAI](https://crewai.io/) library to create an agent specialized in the General Data Protection Law (LGPD). The agent uses language models (LLMs) and PDF documents as knowledge sources to answer questions related to the LGPD.

## Technologies Used
- Python
- [CrewAI](https://crewai.io/)
- Language Models (`gpt-4o-mini`)
- PDF Document Processing (`PDFKnowledgeSource`)

## Installation and Configuration

1. Clone this repository:
```sh
git clone https://github.com/lorenzouriel/crewai-lgpd-specialist.git
cd crewai-lgpd-specialist
```
2. Create a virtual environment and activate it:
```sh
python -m venv venv
source venv/bin/activate # On Windows, use: venv\Scripts\activate
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

4. Run the project:
```sh
streamlit run app.py
```

> Update `.env` with the `OPENAI_API_KEY`!

## How It Works
1. The `specialist_lgpd` agent is created using a language model (`LLM`).
2. It receives PDF documents as a knowledge source.
3. The agent performs the task of answering questions based on the content of the documents.