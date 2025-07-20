
import streamlit as st
from llm_api import generate_reply
import time

st.set_page_config(page_title="Chatbot with Personality", page_icon="🧠", layout="centered")

st.markdown("""
<style>
.chatbox-container {
    padding: 2rem;
    background-color: #1e1e1e;
    border: 1px solid #333;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    margin-bottom: 2rem;
}
.chat-title {
    font-size: 2.2rem;
    font-weight: 700;
    color: #f3f3f3;
    margin-bottom: 0.3rem;
}
.chat-subtitle {
    font-size: 1rem;
    color: #bbbbbb;
    margin-bottom: 1.5rem;
}
.chat-message-user, .chat-message-bot {
    border-radius: 10px;
    padding: 0.75rem 1rem;
    margin-bottom: 0.6rem;
    max-width: 90%;
}
.chat-message-user {
    background-color: #2c3e50;
    color: #ecf0f1;
    align-self: flex-end;
    margin-left: auto;
}
.chat-message-bot {
    background-color: #3a3a3a;
    color: #ffffff;
    align-self: flex-start;
    margin-right: auto;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='chatbox-container'>", unsafe_allow_html=True)
st.markdown("<div class='chat-title'>🧠 Chatbot with Personality Toggle</div>", unsafe_allow_html=True)
st.markdown("<div class='chat-subtitle'>Choose a personality and chat in your preferred style.</div>", unsafe_allow_html=True)

persona = st.selectbox("Select a chatbot personality:", [
    "Friendly Dev 👨‍💻", "Therapist 🛋️", "Sarcastic Bro 😎", "Startup Hustler 🚀", "Nerdy Bot 🤓"
], key="persona")

st.markdown("</div>", unsafe_allow_html=True)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Type your message...")

if user_input:
    with st.spinner("🤖 Typing..."):
        try:
            placeholder = st.empty()
            placeholder.markdown("🤖 is thinking...")
            time.sleep(1.25)

            persona_clean = persona.split(" ")[0]
            bot_reply = generate_reply(persona_clean, user_input)
            placeholder.empty()

            st.session_state.chat_history.append(("user", user_input))
            st.session_state.chat_history.append(("bot", bot_reply))
        except Exception as e:
            st.error(f"Error: {e}")

# Render messages
for sender, msg in st.session_state.chat_history:
    if sender == "user":
        with st.chat_message("user", avatar="🧑"):
            st.markdown(f"<div class='chat-message-user'>{msg}</div>", unsafe_allow_html=True)
    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(f"<div class='chat-message-bot'>{msg}</div>", unsafe_allow_html=True)
