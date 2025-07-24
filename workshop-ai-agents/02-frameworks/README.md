## Como usar

### Pré-requisitos

1. **Instalar Ollama**:
```bash
# Baixar e instalar: https://ollama.ai
ollama serve
ollama pull mistral:latest
```

2. **Instalar dependências**:
```bash
pip install -r requirements.txt
```

### Executar os exemplos
```bash
# Agno - Análise HackerNews
python agno_starter.py

# AutoGen - Colaboração multi-agente
python autoge_starter.py

# CrewAI - Conteúdo LinkedIn
python crewai_starter.py

# LangChain/LangGraph - Pipeline de análise
python langchain_langgraph_starter.py
```

## Configuração
Todos os exemplos estão configurados para usar **Ollama localmente**, não requerendo chaves de API externas.

**URL padrão do Ollama**: `http://localhost:11434`
**Modelo recomendado**: `mistral:latest`

## Conceitos Demonstrados
- **Multi-agent systems**: Diferentes agentes trabalhando em conjunto
- **Especialização de papéis**: Cada agente tem uma função específica
- **Comunicação entre agentes**: Troca de informações e colaboração
- **Fluxos de trabalho**: Sequências organizadas de tarefas
- **Estado compartilhado**: Memória comum entre agentes
- **Integração com ferramentas externas**: APIs e serviços
- **Processamento local**: Sem dependência de APIs pagas

## Quando usar cada framework
- **Agno**: Análise de dados e integração com APIs específicas
- **AutoGen**: Colaboração complexa entre múltiplos agentes
- **CrewAI**: Workflows estruturados com papéis bem definidos
- **LangChain/LangGraph**: Pipelines complexos com visualização e controle de fluxo