from model import llm
from chunk import chunk_text

with open("full_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = chunk_text(text)

summaries = []

for i, chunk in enumerate(chunks):
    print(f"Processing chunk {i+1}/{len(chunks)}")

    prompt = f"""
    Summarize this for a student in simple terms:

    {chunk}
    """

    result = llm(prompt)[0]['generated_text']
    summaries.append(result)

# Save compressed knowledge
with open("knowledge.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(summaries))

print("✅ Knowledge base created")