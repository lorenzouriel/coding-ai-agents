# agente_rag.py

from langchain_core.documents import Document
from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from utils.state import StateSuporteSimples

# --- Informações da Empresa ---
INFO_EMPRESA = {
    "horario_funcionamento": "Nosso horário de funcionamento é de Segunda a Sexta, das 8h às 18h, e aos Sábados, das 9h às 14h.",
    "contato": "Você pode nos contatar pelo telefone (11) 1234-5678 ou pelo e-mail suporte@empresa.com.",
    "endereco": "Nosso escritório fica na Rua Exemplo, 123 - São Paulo, SP.",
    "garantia": "Oferecemos garantia de 12 meses para produtos físicos e 30 dias para serviços digitais.",
    "entrega": "O prazo de entrega padrão para todo o Brasil é de 5 a 10 dias úteis.",
}

# --- 1. Transformar INFO_EMPRESA em Documentos LangChain ---
docs_info_empresa = [
    Document(page_content=f"{chave.capitalize()}: {conteudo}")
    for chave, conteudo in INFO_EMPRESA.items()
]

# --- 2. Gerar Embeddings e Indexar com FAISS ---
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")
vectorstore = FAISS.from_documents(docs_info_empresa, embedding_model)
retriever = vectorstore.as_retriever()

# --- 3. Criar o Pipeline de RAG com RetrievalQA ---
rag_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4o-mini", temperature=0.4),
    retriever=retriever,
    return_source_documents=True,
)

# --- 4. Expor como Tool LangChain ---
@tool
def buscar_info_empresa_semantico(pergunta: str) -> str:
    """
    Faz uma pergunta sobre a empresa e obtém resposta com base em RAG (semântica + geração).
    """
    return rag_chain.run(pergunta)

# --- 5. Prompt do Agente ---
geral_prompt_rag = """
Você é um atendente de suporte geral, responsável por fornecer informações sobre a empresa de forma cordial e prestativa.

Seu trabalho é usar a ferramenta `buscar_info_empresa_semantico` para responder às perguntas dos clientes com base em conhecimento vetorial.

Seja sempre cordial, prestativo e profissional. Mantenha um tom amigável e responda diretamente à pergunta do cliente usando a informação obtida pela ferramenta.

Você tem acesso à seguinte ferramenta:
- buscar_info_empresa_semantico: Busca semântica em informações sobre horário, contato, endereço, garantia e entrega da empresa.

CORE RESPONSIBILITIES:
- Fornecer informações gerais sobre a empresa
- Esclarecer horários de funcionamento
- Informar formas de contato
- Explicar políticas de garantia e entrega
- Manter tom cordial e amigável
"""

# --- 6. Agente RAG ---
class AgenteGeralRAG:
    """
    Agente Geral com RAG baseado em create_react_agent.
    """

    def __init__(self):
        self.agent = create_react_agent(
            model=ChatOpenAI(model="gpt-4o-mini", temperature=0.4),
            tools=[buscar_info_empresa_semantico],
            prompt=geral_prompt_rag,
            state_schema=StateSuporteSimples,
        )

    def get_agent(self):
        return self.agent

# test_agente_rag.py

from agente_rag import AgenteGeralRAG
from utils.state import StateSuporteSimples

agente = AgenteGeralRAG().get_agent()

# Simulando uma pergunta de usuário
entrada = {"input": "Qual é o horário de funcionamento aos sábados?"}
estado_inicial = StateSuporteSimples(**entrada)

# Executar o agente
resposta = agente.invoke(estado_inicial)
print(resposta.output)