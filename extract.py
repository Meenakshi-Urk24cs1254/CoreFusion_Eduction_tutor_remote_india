import fitz  # PyMuPDF

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

text = extract_text("textbook.pdf")
with open("full_text.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("✅ Text extracted")