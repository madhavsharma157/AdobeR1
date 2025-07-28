Adobe-Round1A 📘 Round 1A Submission – Understand Your Document Challenge 🔍 Challenge Summary The goal is to extract a structured outline from PDF documents, including:

Title Headings at levels: H1, H2, H3 Page numbers associated with each heading This enables semantic search, recommendation engines, and other intelligent document features.

📂 Project Structure round1a_final_submission/ │ ├── Dockerfile # Docker container setup ├── extract_outline.py # Python script to extract outlines using PyMuPDF ├── run_instructions.txt # Command-line usage guide │ ├── input/ # Input PDFs to be processed │ ├── Introduction_to_Artificial_Intelligence_H2.pdf │ ├── History_of_AI_H3.pdf │ └── Reaction_Kinetics_Study_Guide.pdf │ └── output/ # JSON output for each input PDF ├── Introduction_to_Artificial_Intelligence_H2.json ├── History_of_AI_H3.json └── Reaction_Kinetics_Study_Guide.json

yaml Copy Edit

⚙️ How to Run

Build the Docker image docker build --platform linux/amd64 -t docoutline:latest .
Run the container bash Copy Edit docker run --rm
-v $(pwd)/input:/app/input
-v $(pwd)/output:/app/output
--network none
docoutline:latest 🔒 No internet/network access — fully offline ✅ Works on linux/amd64, CPU-only environment
🧠 Technology Stack Python 3.9

PyMuPDF (for PDF text structure parsing)

Docker (slim image) – for compact, portable runtime

✅ Output Format Each PDF generates a matching .json file with:

json Copy Edit { "title": "Document Title", "outline": [ { "level": "H1", "text": "Section Title", "page": 1 }, { "level": "H2", "text": "Subsection Title", "page": 2 }, { "level": "H3", "text": "Nested Subsection", "page": 3 } ] } 📈 Performance & Constraints ⏱️ Execution time: < 10 seconds per 50-page PDF

💾 No model > 200MB used

🖥️ CPU-only (no GPU needed)

🌐 Fully offline (no internet access)

👤 Authors & Contributors Submission prepared for Hackathon Round 1A
