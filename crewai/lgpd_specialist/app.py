import streamlit as st
from main import run_specialist_crew

st.set_page_config(page_title="Specialist Crew LGPD", layout="wide")

st.title("📜 Especialista Crew LGPD")
st.write("🔍 Faça perguntas sobre a LGPD e obtenha respostas especializadas.")

with st.sidebar:
    st.header("⚙️ Configurações")
    st.write("Escolha a tarefa que deseja realizar:")
    task_type = "📌 Responder Pergunta sobre LGPD"

    user_question = st.text_area("✍️ Digite sua pergunta sobre LGPD:", height=150)

if st.button("🔎 Obter Resposta"):
    if not user_question.strip():
        st.warning("⚠️ Por favor, digite uma pergunta antes de continuar.")
    else:
        st.info("⏳ Processando sua solicitação... Aguarde um momento.")
        with st.spinner("Buscando resposta..."):
            result = run_specialist_crew(user_question)

        st.subheader("📌 Resposta Especialista:")
        st.write(result)

st.markdown("---")
st.caption("🔹 Powered by CrewAI | Desenvolvido por Lorenzo Uriel 🚀")