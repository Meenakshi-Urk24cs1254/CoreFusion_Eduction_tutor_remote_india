from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

# Load textbook
with open("science.txt", "r", encoding="utf-8") as f:
    textbook = f.read()

query = input("Ask your question: ")

# Context pruning
relevant_text = ""

for line in textbook.split("\n"):
    if any(word in line.lower() for word in query.lower().split()):
        relevant_text += line + "\n"

relevant_text = relevant_text[:300]

prompt = f"""
Answer using ONLY this content:

{relevant_text}

Question: {query}
"""

response = client.chat.completions.create(
    model="openrouter/auto",   # FREE model
    messages=[{"role": "user", "content": prompt}]
)

print("\nAnswer:\n")
print(response.choices[0].message.content)