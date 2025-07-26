# Ollama Playground

A minimal playground for experimenting with custom LLaMA 3 assistants using [Ollama](https://ollama.com/).

This setup includes **Axon**, a smart, succinct, and informative assistant based on `llama3.2`.

## Getting Started

1. Install [Ollama](https://ollama.com/download)
2. Clone this repo:
   ```bash
   git clone https://github.com/Rohan-Shakya/ollama-playground.git
   cd ollama-playground
   ```
3. Build and run:
   ```
   ollama create axon -f Modelfile
   ollama run axon
   ```

## REST API Example

Once the assistant is running, you can interact with it via the REST API.

Example Request
To generate a response from the assistant, send a POST request to:

```
POST http://localhost:11434/api/generate
```

With the following JSON body:

```
{
  "model": "axon",
  "prompt": "Hello, tell me about the LLaMA model.",
  "stream": false
}
```

- model: The name of the model to use (e.g., "axon").
- prompt: The prompt you want the assistant to respond to.
- stream: Whether to stream the response or wait for the complete result (false means you’ll get the full response in one go).

## Example cURL Command:

```
curl -X POST http://localhost:11434/api/generate -H "Content-Type: application/json" -d '{"model": "axon", "prompt": "Tell me about the LLaMA model.", "stream": false}'

```

> This will return the generated response from the assistant.
