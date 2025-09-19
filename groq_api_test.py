import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("Error: GROQ_API_KEY not found in .env file.")
    exit()

print(f"Testing with API Key ending: ...{api_key[-4:]}")

# 1. List all available models
models_url = "https://api.groq.com/openai/v1/models"
headers = {"Authorization": f"Bearer {api_key}"}

print("\n--- Checking available models ---")
try:
    resp = requests.get(models_url, headers=headers)
    print(f"Status: {resp.status_code}")
    resp.raise_for_status()
    models = resp.json()
    print(json.dumps(models, indent=2))
except Exception as e:
    print(f"Error fetching models: {e}")
    if hasattr(e, 'response') and e.response is not None:
        print(e.response.text)

# 2. Try a chat completion with the user's requested model
model_id = "meta-llama/llama-4-maverick-17b-128e-instruct"
chat_url = "https://api.groq.com/openai/v1/chat/completions"
headers["Content-Type"] = "application/json"

payload = {
    "model": model_id,
    "messages": [
        {"role": "user", "content": "Say hello and state your model name."}
    ]
}

print(f"\n--- Testing chat completion with model: {model_id} ---")
try:
    resp = requests.post(chat_url, headers=headers, data=json.dumps(payload))
    print(f"Status: {resp.status_code}")
    resp.raise_for_status()
    print(json.dumps(resp.json(), indent=2))
except Exception as e:
    print(f"Error with chat completion: {e}")
    if hasattr(e, 'response') and e.response is not None:
        print(e.response.text)
