import streamlit as st
from main import run_junior_support_crew

st.set_page_config(page_title="Junior Support Chatbot", layout="wide")

st.title("💬 Junior Support Chatbot")
st.write("🔍 Ask questions about the system and get helpful responses.")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("⚙️ Settings")
    st.write("Choose the task you want to perform:")
    task_type = "📌 Answer System FAQ"

# User input
user_question = st.text_area("✍️ Type your question:", height=120)

if st.button("💡 Send"):
    if not user_question.strip():
        st.warning("⚠️ Please type a question before sending.")
    else:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_question})

        # Show processing spinner
        with st.spinner("⏳ Processing..."):
            # Run the Junior Support Crew
            response = run_junior_support_crew(user_question)
            st.session_state.messages.append({"role": "assistant", "content": response})

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**Support Bot:** {message['content']}")

st.markdown("---")
st.caption("Developed by Lorenzo Uriel 🚀")