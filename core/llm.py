import requests
from core.config import OLLAMA_URL, OLLAMA_MODEL

SYSTEM_PROMPT = "You are a helpful offline voice assistant. Keep answers concise and conversational."

def chat(user_input: str, history: list = []) -> str:
    conversation = SYSTEM_PROMPT + "\n\n"
    for turn in history[-6:]:
        conversation += f"User: {turn['user']}\nAssistant: {turn['assistant']}\n"
    conversation += f"User: {user_input}\nAssistant:"

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": conversation,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        result = response.json()
        reply = result.get("response", "").strip()
        print(f"🤖 Agent: {reply}")
        return reply
    except requests.exceptions.ConnectionError:
        return "Error: Ollama is not running. Please start it with 'ollama serve'."
    except Exception as e:
        return f"Error: {str(e)}"
