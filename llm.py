import os
import requests
from dotenv import load_dotenv

load_dotenv()

def call_llm(prompt):

    key = os.getenv("OPENROUTER_API_KEY")

    if not key:
        return "⚠️ API key missing"

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)

        if response.status_code != 200:
            return f"⚠️ API Error: {response.text}"

        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"⚠️ LLM error: {str(e)}"