import requests
from dotenv import load_dotenv
import os

load_dotenv() 

def ask_jarvis(question):
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = "openai/gpt-oss-20b" 

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Tu es JARVIS. Tu dois répondre EXCLUSIVEMENT en français, de manière concise et polie. Ne réponds jamais dans une autre langue et ne dépasse pas les 80 tokens pour tes réponses"},
            {"role": "user", "content": question}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        print(response.status_code)
        print(response.text)  # check this if something goes wrong, before raise_for_status
        response.raise_for_status()
        data = response.json()
        text = data["choices"][0]["message"]["content"]
        print(text)

        return text
    except Exception as e:
        return f"Erreur de communication: {e}"