# Specialist Crew - LGPD Assistant

Este projeto utiliza a biblioteca [CrewAI](https://crewai.io/) para criar um agente especializado na Lei Geral de Proteção de Dados (LGPD). O agente utiliza modelos de linguagem (LLMs) e documentos PDF como fonte de conhecimento para responder perguntas relacionadas à LGPD.

## Tecnologias Utilizadas
- Python
- [CrewAI](https://crewai.io/)
- Modelos de linguagem (`gpt-4o-mini`)
- Processamento de documentos PDF (`PDFKnowledgeSource`)

## Instalação e Configuração

1. Clone este repositório:
```sh
git clone https://github.com/lorenzouriel/crewai-lgpd-specialist.git
cd crewai-lgpd-specialist
```
2. Crie um ambiente virtual e ative-o:
```sh
python -m venv venv
 source venv/bin/activate  # No Windows, use: venv\Scripts\activate
```

3. Instale as dependências:
```sh
pip install -r requirements.txt
```

4. Execute o projeto:
```sh
streamlit run app.py
```

> Atualize o `.env` com a `OPENAI_API_KEY`!

## Como Funciona
1. O agente `specialist_lgpd` é criado utilizando um modelo de linguagem (`LLM`).
2. Ele recebe documentos PDF como fonte de conhecimento.
3. O agente executa a tarefa de responder perguntas com base no conteúdo dos documentos.