import psycopg2   # Biblioteca para conectar e interagir com o banco de dados PostgreSQL
from psycopg2 import sql   # Permite construir consultas SQL de forma segura e dinâmica
from contract import Vendas   # Importa a classe ou função 'Vendas' do módulo 'contract'
import streamlit as st   # Framework para criar interfaces web interativas, usado principalmente para aplicativos de data science
from dotenv import load_dotenv   # Biblioteca para carregar variáveis de ambiente a partir de um arquivo .env
import os   # Módulo padrão do Python para interagir com o sistema operacional, usado para acessar variáveis de ambiente

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Acessar as variáveis de ambiente
DB_HOST = os.getenv("DB_HOST")   # Obtém o endereço do servidor do banco de dados
DB_NAME = os.getenv("DB_NAME")   # Obtém o nome do banco de dados
DB_USER = os.getenv("DB_USER")   # Obtém o nome do usuário do banco de dados
DB_PASS = os.getenv("DB_PASS")   # Obtém a senha do usuário do banco de dados

# Função para salvar os dados validados no PostgreSQL
def save_to_database(dados:Vendas):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()
        
        # Inserção dos dados na tabela de vendas
        insert_query = sql.SQL(
            "INSERT INTO vendas (email, data, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s)"
        )

        cursor.execute(insert_query, (
            dados.email,
            dados.data,
            dados.valor,
            dados.quantidade,
            dados.produto.value
        ))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Command Executed Succesfully!")
        
    except Exception as e:
        st.error(f"Error on Executing Command: {e}")