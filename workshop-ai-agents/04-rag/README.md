# 🔍 04-RAG - Retrieval-Augmented Generation

Esta pasta contém uma implementação educacional completa de **Retrieval-Augmented Generation (RAG)**, demonstrando cada etapa do processo desde o carregamento de documentos até a geração de respostas contextuais usando tanto **Ollama** (local) quanto **OpenAI**.

## 🎯 Objetivo Educacional

Demonstrar na prática todos os conceitos fundamentais de RAG através de exemplos progressivos, desde conceitos básicos até implementação completa, focando em:
- **Pipeline RAG completo** passo-a-passo
- **Chunking inteligente** e suas implicações
- **Embeddings vetoriais** e busca semântica
- **Avaliação de qualidade** com métricas
- **Otimização de performance** e debugging

## Estrutura dos Arquivos

### Pipeline Completo
| Arquivo | Descrição | Nível |
|---------|-----------|-------|
| **`RAG_pipeline.py`** | Sistema RAG completo e funcional | ⭐⭐⭐ **Principal** |

### Conceitos Detalhados (Step-by-Step)
| Arquivo | Conceito | Foco Educacional |
|---------|----------|------------------|
| **`chunking-example.py`** | Text Chunking | Como texto é dividido e impactos |
| **`embedding-example.py`** | Vector Embeddings | Como texto vira números |
| **`semantic-search-example.py`** | Busca Semântica | Similaridade vs palavras-chave |
| **`context_enrichment.py`** | Context Enrichment | Preparação para geração |

### Dataset e Avaliação
| Item | Descrição |
|------|-----------|
| **`data/Understanding_Climate_Change.pdf`** | Documento exemplo para demonstrações |
| **`db/`** | Bancos vetoriais (Chroma + FAISS) |

## Pipeline RAG Detalhado

### Step 1: Document Loading
```python
# Carregamento de PDF com metadados
loader = PyPDFLoader(file_path)
documents = loader.load()
```
**Conceitos:** Processamento de documentos, preservação de metadados

### Step 2: Text Chunking
```python
# Divisão inteligente com overlap
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,      # Tamanho do chunk
    chunk_overlap=200,    # Sobreposição para contexto
    separators=["\n\n", "\n", " ", ""]  # Hierarquia de separação
)
```
**Conceitos:** Balanceamento contexto vs precisão, continuidade semântica

### Step 3: Vector Embeddings
```python
# Conversão texto → vetores
embeddings_model = OllamaEmbeddings(model="mxbai-embed-large")
vectorstore = Chroma.from_documents(documents, embeddings_model)
```
**Conceitos:** Representação semântica, similaridade cosine

### Step 4: Semantic Search
```python
# Busca por similaridade
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}  # Top 5 resultados
)
```
**Conceitos:** Relevância semântica vs sintática

### Step 5: Context Enrichment
```python
# Preparação do contexto
context = "\n\n".join([doc.page_content for doc in relevant_docs])
```
**Conceitos:** Otimização de context window

### Step 6: Answer Generation
```python
# Geração com contexto
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)
response = llm.invoke([SystemMessage(context), HumanMessage(query)])
```
**Conceitos:** Prompt engineering para RAG

## Como Usar

### 1. Configuração Inicial

```bash
# 1. Instalar Ollama (Opcional para uso local)
curl -fsSL https://ollama.ai/install.sh | sh
ollama serve
ollama pull mxbai-embed-large:latest
ollama pull mistral:latest

# 2. Instalar dependências Python
pip install -r requirements.txt

# 3. Configurar APIs (opcional)
export OPENAI_API_KEY="sua-chave-openai"
export TAVILY_API_KEY="sua-chave-tavily"  # Para busca web
```

### 2. Executar Pipeline Completo

```bash
# RAG completo com interface interativa
python RAG_pipeline.py

# Escolher durante execução:
# 1. Apenas Ollama (100% local, gratuito)
# 2. Ollama + OpenAI (embeddings locais, geração OpenAI)
```

### 3. Explorar Conceitos Individuais

```bash
# Entender chunking
python chunking-example.py

# Ver embeddings em ação
python embedding-example.py

# Comparar busca semântica vs tradicional
python semantic-search-example.py

# Analisar enriquecimento de contexto
python context_enrichment.py
```

## Tecnologias e Modelos

### Modelos de Embedding
| Modelo | Dimensões | Idioma | Velocidade | Qualidade |
|--------|-----------|--------|------------|-----------|
| **mxbai-embed-large** | 1024 | Multilingual | 🚀 Rápido | ⭐⭐⭐⭐⭐ |
| **text-embedding-3-small** | 1536 | Multilingual | 🌐 API | ⭐⭐⭐⭐ |

### Vector Stores
| Store | Uso | Performance | Persistência |
|-------|-----|-------------|--------------|
| **Chroma** | Desenvolvimento | 🚀 Rápido | ✅ Local |
| **FAISS** | Produção | ⚡ Ultra-rápido | ✅ Local |

### LLMs Suportados
- **Ollama Local**: mistral, llama2, deepseek-r1
- **OpenAI**: gpt-3.5-turbo, gpt-4
- **Configurável**: Temperatura, max_tokens, etc.

## Parâmetros de Otimização

### Chunking Strategy
```python
# Configuração recomendada
chunk_size = 1000        # Balanço contexto/precisão
chunk_overlap = 200      # 20% overlap para continuidade
separators = ["\n\n", "\n", " "]  # Hierárquica
```

### Retrieval Configuration
```python
# Busca otimizada
search_type = "similarity"    # vs "mmr" (diversidade)
k = 5                        # Número de chunks
score_threshold = 0.7        # Filtro de relevância
```

### Generation Settings
```python
# LLM para geração
temperature = 0.3            # Balanço precisão/criatividade
max_tokens = 1000           # Limite de resposta
top_p = 0.9                 # Nucleus sampling
```

## Análise de Performance

### Métricas de Qualidade

**Retrieval Metrics:**
- **Precision@k**: Relevância dos top-k chunks
- **Recall@k**: Cobertura de informação relevante
- **MRR**: Mean Reciprocal Rank

**Generation Metrics:**
- **Faithfulness**: Fidelidade ao contexto recuperado
- **Relevancy**: Relevância contextual da resposta
- **Correctness**: Precisão factual

### Debugging RAG
**Problemas Comuns e Soluções:**
1. **Chunks Irrelevantes**
   ```python
   # Solução: Ajustar chunking
   chunk_size = 1500  # Mais contexto
   chunk_overlap = 300  # Mais continuidade
   ```

2. **Contexto Insuficiente** 
   ```python
   # Solução: Mais chunks
   search_kwargs = {"k": 8}  # Mais resultados
   ```

3. **Respostas Inconsistentes**
   ```python
   # Solução: Menor temperatura
   temperature = 0.1  # Mais determinístico
   ```

## Casos de Uso Ideais
### Ótimo para RAG
- **Documentação técnica**: APIs, manuais, guias
- **Base de conhecimento**: FAQ, políticas, procedimentos  
- **Pesquisa acadêmica**: Papers, relatórios, estudos
- **Conteúdo empresarial**: Relatórios, apresentações

### Limitações do RAG
- **Informações desatualizadas**: RAG é estático
- **Raciocínio complexo**: Melhor usar fine-tuning
- **Dados estruturados**: Considerar SQL/GraphRAG
- **Tempo real**: Informações dinâmicas

## Experimentos e Extensões
### Técnicas Avançadas (Para Estudo)
1. **Advanced Chunking**:
   - Semantic chunking (por tópicos)
   - Document-aware splitting
   - Hierarchical chunking

2. **Retrieval Enhancement**:
   - Hybrid search (semântica + palavra-chave)
   - Reranking models
   - Query expansion/reformulation

3. **Context Optimization**:
   - Context compression
   - Relevant sentence extraction
   - Multi-hop reasoning

4. **Evaluation Framework**:
   - Human evaluation
   - A/B testing
   - Domain-specific metrics

## Conceitos Demonstrados
### Para Estudantes
- **Vector databases**: Armazenamento e busca eficiente
- **Embedding models**: Representação semântica de texto
- **Similarity search**: Recuperação por significado
- **Context window management**: Otimização de prompt
- **Local vs Cloud**: Trade-offs Ollama vs OpenAI
- **Evaluation frameworks**: Métricas de qualidade

### Para Pesquisadores
- **Information retrieval**: Técnicas de recuperação
- **Neural embeddings**: Representações distribuídas
- **Prompt engineering**: Otimização de instruções
- **Performance optimization**: Tuning de hiperparâmetros
