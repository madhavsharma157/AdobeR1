import os
import json
import fitz  # PyMuPDF

def extract_outline_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    toc = doc.get_toc(simple=True)
    title = os.path.splitext(os.path.basename(pdf_path))[0]
    outline = []
    for entry in toc:
        level, text, page = entry
        outline.append({ "level": f"H{level}", "text": text, "page": page })
    return { "title": title, "outline": outline }

input_dir = "/app/input"
output_dir = "/app/output"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(input_dir, filename)
        outline = extract_outline_from_pdf(pdf_path)
        output_filename = os.path.splitext(filename)[0] + ".json"
        with open(os.path.join(output_dir, output_filename), "w") as f:
            json.dump(outline, f, indent=4)