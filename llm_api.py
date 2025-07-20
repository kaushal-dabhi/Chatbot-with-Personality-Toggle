
import requests
import streamlit as st

# Define personality system prompts
PERSONALITY_PRESETS = {
    "Friendly Dev": "You are a warm, helpful developer who loves pair programming.",
    "Therapist": "You are a calm, supportive therapist who listens empathetically and gives thoughtful advice.",
    "Sarcastic Bro": "You are witty, sarcastic, and always have a playful comeback.",
    "Startup Hustler": "You speak like a Silicon Valley founder, full of buzzwords and optimism.",
    "Nerdy Bot": "You respond with technical depth, references, and a love for scientific accuracy."
}

def generate_reply(persona, user_message):
    api_url = "https://api.groq.com/openai/v1/chat/completions"
    api_key = st.secrets.get("GROQ_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": PERSONALITY_PRESETS.get(persona, "")},
            {"role": "user", "content": user_message}
        ],
        "max_tokens": 200,
        "temperature": 0.7
    }

    response = requests.post(api_url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
