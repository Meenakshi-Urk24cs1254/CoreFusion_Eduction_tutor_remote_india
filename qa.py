from model import llm

with open("knowledge.txt", "r", encoding="utf-8") as f:
    knowledge = f.read()

def ask(question):
    prompt = f"""
    You are a helpful tutor.

    Use this knowledge to answer:

    {knowledge}

    Question: {question}
    """

    result = llm(prompt)[0]['generated_text']
    return result

# Test
while True:
    q = input("Ask: ")
    print(ask(q))