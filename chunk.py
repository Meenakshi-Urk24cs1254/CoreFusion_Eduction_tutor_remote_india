def chunk_text(text, size=1000):
    return [text[i:i+size] for i in range(0, len(text), size)]

with open("full_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = chunk_text(text)

print("Total chunks:", len(chunks))