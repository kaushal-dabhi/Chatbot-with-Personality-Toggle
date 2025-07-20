
# 🤖 Chatbot with Personality Toggle

A Streamlit app powered by Groq's LLaMA 3, allowing users to chat with different AI personas.

## 🧠 Features
- Choose from 5 personalities (Dev, Therapist, Bro, Hustler, Nerd)
- Real-time chat powered by `llama3-8b-8192`
- Stateless backend (session-based chat)
- Clean UI with `streamlit.chat_input`

## 🚀 Run Locally

1. Clone the repo  
2. Create `.streamlit/secrets.toml` with:

```
GROQ_API_KEY = "your_groq_api_key_here"
```

3. Run:

```bash
streamlit run app.py
```

## 🌐 Deploy to Streamlit Cloud

- Push to GitHub
- Connect repo at https://streamlit.io/cloud
- Add `GROQ_API_KEY` to the secrets manager
