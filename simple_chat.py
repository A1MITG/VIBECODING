import os
import requests
from dotenv import load_dotenv

load_dotenv()

def simple_chat():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("GROQ_API_KEY not found in .env file.")
        return
    
    print("Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        payload = {
            "model": "meta-llama/llama-4-maverick-17b-128e-instruct",
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        try:
            resp = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
            resp.raise_for_status()
            data = resp.json()
            print("Bot:", data['choices'][0]['message']['content'])
        except Exception as e:
            print("Error:", e)
            if hasattr(e, 'response') and e.response is not None:
                print(e.response.text)

if __name__ == "__main__":
    simple_chat()
