import requests
import json

def fetch_response(url, data):
    """Send a POST request to the API and return the streamed response."""
    try:
        response = requests.post(url, json=data, stream=True)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def display_generated_text(response):
    """Iterate over the streamed response and print the generated text."""
    print("Generated Text:", end=" ", flush=True)
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode("utf-8")
            try:
                result = json.loads(decoded_line)
                generated_text = result.get("response", "")
                print(generated_text, end="", flush=True)
            except json.JSONDecodeError:
                print("Error: Failed to decode JSON response.")
                break
    print()

url = "http://localhost:11434/api/generate"
data = {
    "model": "llama3.2",
    "prompt": "tell me a short story and make it funny.",
}

response = fetch_response(url, data)

if response:
    display_generated_text(response)
else:
    print("Error: No valid response from the API.")
