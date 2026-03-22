from flask import Flask, request, render_template
from model import llm

app = Flask(__name__)

with open("knowledge.txt", "r", encoding="utf-8") as f:
    knowledge = f.read()

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]

        prompt = f"""
        Answer clearly using this knowledge:

        {knowledge}

        Question: {question}
        """

        answer = llm(prompt)[0]['generated_text']

    return f"""
    <form method="post">
        <input name="question" placeholder="Ask question">
        <input type="submit">
    </form>
    <p>{answer}</p>
    """

app.run(debug=True)