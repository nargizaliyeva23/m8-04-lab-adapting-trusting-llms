from openai import OpenAI

# -----------------------------
# Connect to local Ollama server
# -----------------------------
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # dummy key (Ollama ignores it)
)

# -----------------------------
# Send chat request
# -----------------------------
response = client.chat.completions.create(
    model="llama3.2:3b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain what an API is in one sentence."}
    ],
    temperature=0.2
)

# -----------------------------
# Print response
# -----------------------------
print("\nMODEL RESPONSE:\n")
print(response.choices[0].message.content)