import ollama

def list_models():
    """List all available models."""
    try:
        response = ollama.list()
        print("Available models:", response)
    except Exception as e:
        print(f"Error listing models: {e}")

def chat_example():
    """Send a chat message to the model and print the response."""
    try:
        res = ollama.chat(
            model="llama3.2",
            messages=[
                {"role": "user", "content": "why is the sky blue?"},
            ],
        )
        print("Chat Response:", res["message"]["content"])
    except Exception as e:
        print(f"Error during chat: {e}")

def chat_streaming_example():
    """Send a chat message with a streaming response to the model."""
    try:
        res = ollama.chat(
            model="llama3.2",
            messages=[
                {"role": "user", "content": "why is the ocean so salty?"},
            ],
            stream=True,
        )
        print("Streaming Response:", end=" ", flush=True)
        # Streaming the response as it arrives
        for chunk in res:
            print(chunk["message"]["content"], end="", flush=True)
        print()
    except Exception as e:
        print(f"Error during streaming: {e}")

def generate_example():
    """Generate text using the model."""
    try:
        res = ollama.generate(
            model="llama3.2",
            prompt="why is the sky blue?",
        )
        print("Generated Text:", res["response"])
    except Exception as e:
        print(f"Error generating text: {e}")

def create_and_use_model():
    """Create a custom model based on 'llama3.2' and generate text using it."""
    
    system_prompt = """
    You are a very smart assistant who knows everything about oceans. You are very succinct and informative.
    """
    
    parameters = {"temperature": 0.1}

    try:
        ollama.create(
            model="inspira", 
            from_="llama3.2", 
            system=system_prompt,
            parameters=parameters
        )
        print("Model 'inspira' created successfully.")

        res = ollama.generate(model="inspira", prompt="why is the ocean so salty?")
        print("Generated Text from 'inspira':", res["response"])

        # Delete the custom model after use
        ollama.delete("inspira")
        print("Model 'inspira' has been deleted.")

    except Exception as e:
        print(f"Error creating or generating text with model 'inspira': {e}")
        try:
            ollama.delete("inspira")
            print("Model 'inspira' has been deleted (partial creation).")
        except Exception as delete_error:
            print(f"Error deleting model 'inspira': {delete_error}")

def main():
    """Execute the workflow."""
    list_models()
    chat_example()
    chat_streaming_example()
    generate_example()
    create_and_use_model()

if __name__ == "__main__":
    main()
