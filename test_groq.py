import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("Error: GROQ_API_KEY not found in .env file.")
    exit()

# Print the last 4 characters of the key for verification, not the whole key.
print(f"Attempting to use API Key ending in: ...{api_key[-4:]}")

api_url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "messages": [
        {
            "role": "user",
            "content": "Explain the importance of low-latency LLMs in 50 words.",
        }
    ],
                "model": "meta-llama/llama-4-maverick-17b-128e-instruct",
}

print("\nSending a test request to the Groq API...")

try:
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    
    print(f"Response Status Code: {response.status_code}")
    
    # Raise an exception for bad status codes (4xx or 5xx) to catch errors
    response.raise_for_status()
    
    print("\nAPI call successful! Response:")
    # Pretty-print the JSON response
    print(json.dumps(response.json(), indent=2))

except requests.exceptions.HTTPError as e:
    print(f"\n--- ERROR: An HTTP error occurred ---")
    print(f"Error Details: {e}")
    # Print the raw response body which often contains useful error details
    print(f"Raw Response Body: {e.response.text}")
except requests.exceptions.RequestException as e:
    print(f"\n--- ERROR: A network request error occurred ---")
    print(f"Error Details: {e}")
