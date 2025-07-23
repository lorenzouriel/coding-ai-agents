import streamlit as st
from contract import Vendas, ProdutoEnum
from database import save_to_database
from pydantic import ValidationError
from datetime import datetime, time

# Função principal para o frontend e validação
def main():
    st.title("Sistema de CRM e Vendas")

    # Campos de entrada para os dados
    email = st.text_input("Email do Vendedor")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9, 0))  # Valor padrão: 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto = st.selectbox("Produto", options=[e.value for e in ProdutoEnum])
    
    # Botão de submissão
    if st.button("Salvar"):
        try:
            # Combinando a data e hora selecionadas para criar o datetime
            data_hora = datetime.combine(data, hora)

            # Validando os dados com Pydantic
            venda = Vendas(
                email=email,
                data=data_hora,
                valor=valor,
                quantidade=quantidade,
                produto=produto
            )
            
            # Salvando os dados no PostgreSQL
            save_to_database(venda)
            st.success("Data Validate and Saved!")

        except ValidationError as e:
            st.error(f"Error on Data Validation: {e}")

        except Exception as e:
            st.error(f"Error on Saving to Database: {e}")

if __name__ == "__main__":
    main()  
