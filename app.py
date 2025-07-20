
import streamlit as st
from llm_api import generate_reply
import time

st.set_page_config(page_title="Chatbot with Personality", page_icon="🧠", layout="centered")

# Persona data
personas = {
    "👨‍💻 Friendly Dev": "Friendly Dev",
    "🛋️ Therapist": "Therapist",
    "😎 Sarcastic Bro": "Sarcastic Bro",
    "🚀 Startup Hustler": "Startup Hustler",
    "🤓 Nerdy Bot": "Nerdy Bot"
}

if "selected_persona" not in st.session_state:
    st.session_state.selected_persona = list(personas.keys())[0]

# Style for persona buttons and overall layout
st.markdown("""
<style>
.chatbox-container {
    padding: 1.5rem;
    background-color: #1e1e1e;
    border: 1px solid #333;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    margin-bottom: 2rem;
}
.chat-title {
    font-size: 2rem;
    font-weight: 700;
    color: #f3f3f3;
    margin-bottom: 0.2rem;
    text-align: center;
}
.chat-subtitle {
    font-size: 0.95rem;
    color: #bbbbbb;
    margin-bottom: 1.2rem;
    text-align: center;
}
.persona-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.5rem;
    margin-bottom: 1rem;
}
.persona-button {
    background-color: #2a2a2a;
    color: #f1f1f1;
    border: 1px solid #444;
    border-radius: 10px;
    padding: 0.6rem 1.2rem;
    font-size: 0.95rem;
    cursor: pointer;
    transition: 0.2s ease;
}
.persona-button:hover {
    background-color: #1abc9c;
    color: black;
}
.persona-selected {
    background-color: #1abc9c;
    color: black;
    font-weight: bold;
    border: 1px solid #1abc9c;
}
.chat-message-user, .chat-message-bot {
    border-radius: 10px;
    padding: 0.75rem 1rem;
    margin-bottom: 0.6rem;
    max-width: 100%;
    word-wrap: break-word;
    font-size: 0.96rem;
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
st.markdown("<div class='chat-subtitle'>Choose how you want the bot to behave below:</div>", unsafe_allow_html=True)

# Persona button grid
st.markdown("<div class='persona-grid'>", unsafe_allow_html=True)
for icon, name in personas.items():
    btn_class = "persona-button"
    if st.session_state.selected_persona == icon:
        btn_class += " persona-selected"
    if st.button(f"{icon} {name}", key=icon):
        st.session_state.selected_persona = icon
st.markdown("</div>", unsafe_allow_html=True)

# Start chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    with st.spinner("🤖 Typing..."):
        try:
            persona_clean = st.session_state.selected_persona.split(" ")[1]
            full_reply = generate_reply(persona_clean, user_input)
            st.session_state.chat_history.append(("bot", full_reply))
        except Exception as e:
            st.error(f"Error: {e}")

for i, (sender, msg) in enumerate(st.session_state.chat_history):
    if sender == "user":
        with st.chat_message("user", avatar="🧑"):
            st.markdown(f"<div class='chat-message-user'>{msg}</div>", unsafe_allow_html=True)
    else:
        with st.chat_message("assistant", avatar="🤖"):
            if i == len(st.session_state.chat_history) - 1 and user_input:
                display = st.empty()
                reply_so_far = ""
                for char in msg:
                    reply_so_far += char
                    display.markdown(f"<div class='chat-message-bot'>{reply_so_far}</div>", unsafe_allow_html=True)
                    time.sleep(0.01)
            else:
                st.markdown(f"<div class='chat-message-bot'>{msg}</div>", unsafe_allow_html=True)

# Back to website
st.markdown("---")
st.markdown(
    "<div style='text-align: center; margin-top: 1.5rem;'>"
    "<a href='https://kaushaldabhi.com' target='_blank' style='padding: 0.6rem 1.2rem; "
    "background-color: #1abc9c; color: black; font-weight: bold; border-radius: 8px; text-decoration: none;'>"
    "← Back to kaushaldabhi.com</a></div>",
    unsafe_allow_html=True
)
