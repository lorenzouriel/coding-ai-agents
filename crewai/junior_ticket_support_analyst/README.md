# Junior Ticket Support Analyst
An AI-powered **junior support assistant** built with [CrewAI](https://github.com/joaomdmoura/crewAI) and Streamlit.  

This chatbot helps answer **frequently asked questions (FAQs)** and provides **step-by-step troubleshooting guidance** for company systems, based on structured documentation (`PDFs`, `Markdown guides`, and `FAQs`).

## Features
- **AI-powered Support**: Answers FAQs and common troubleshooting questions.
- **Knowledge Sources**: Uses company manuals, setup guides, troubleshooting docs, and culture code.
- **Chat Interface**: Simple Streamlit frontend for interaction.
- **Scalable CrewAI Agents**: Modular design with agents and tasks.
- **Multi-format Knowledge**: Supports `.pdf` and `.md` documents as knowledge sources.

## Project Structure
```bash
junior_ticket_support_analyst/
├── app.py                      # Streamlit app (chat interface)
├── main.py                     # Entry point to run the crew
├── crew.py                     # CrewAI agents and tasks definition
├── config/
│   ├── agents.yaml             # Agent roles, goals, and backstories
│   ├── tasks.yaml              # Task definitions
├── knowledge/
│   ├── system_manual.pdf           # System manual (knowledge source)
│   ├── culture_code.pdf            # Company culture code
│   ├── setup_guide.md              # Setup instructions
│   ├── troubleshooting.md          # Troubleshooting guide
│   ├── feature_faq.md              # FAQ about features
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies
```

## Installation
1. **Clone the repository**
```bash
git clone https://github.com/lorenzouriel/coding-ai-agents.git
cd coding-ai-agents\crewai\junior_ticket_support_analyst
```

2. **Create a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Add knowledge source files**
* Place your `system_manual.pdf`, `culture_code.pdf`, and `.md` guides inside the project root.

## Running the App
Start the chatbot locally with:
```bash
streamlit run app.py
```

* Local URL: [http://localhost:8502](http://localhost:8502)
* Network URL: `http://<your-ip>:8502`

## How It Works

* **Agent:** `junior_ticket_support_agent`
  * Role: Junior Ticket Support Analyst
  * Goal: Provide clear and concise answers using the company’s knowledge base.
  * Backstory: Works at the IT helpdesk, focuses on FAQs, and escalates complex issues.

* **Task:** `answer_system_faq`
  * Handles user queries (*“How do I reset my password?”*).
  * Produces step-by-step responses based on documentation.

## Knowledge Sources
* `system_manual.pdf` → Official system guide.
* `culture_code.pdf` → Company culture & values.
* `setup_guide.md` → Environment setup instructions.
* `troubleshooting.md` → Common problems & solutions.
* `feature_faq.md` → List of frequently asked questions.