# Resume-Matcher

A **Python-based Resume Matcher** that evaluates how well a candidate's resume fits a job description using **NLP, TF-IDF, Semantic Similarity, and Skill Extraction**.  
Supports **PDF and TXT resumes**, dynamic skill matching, and an **interactive CLI**.

---

## Features

- Compute **TF-IDF similarity** between resume and job description.
- Compute **Semantic similarity** using **Sentence Transformers**.
- Extract technical skills dynamically from resumes and job descriptions.
- Handles complex skills like **CI/CD, REST API, Node.js, C++**, etc.
- Interactive CLI to select resumes and job descriptions.
- Supports **PDF and TXT formats**.

---

## Project Structure

resume-matcher/
│
├── data/
│ ├── job_descriptions/
│ │ ├── jd1.txt
│ │ ├── jd2.txt
│ │ └── jd3.txt
│ └── resumes/
│ ├── resume1.txt
│ └── resume2.txt
│
├── src/
│ ├── init.py
│ ├── cli.py
│ ├── matcher.py
│ ├── nlp_utils.py
│ ├── parser.py
│ └── pdf_utils.py
│
├── LICENSE
├── README.md
├── main.py
└── requirements.txt

---

## Installation

1. Clone the repository:

git clone https://github.com/shabbirbasha-dev/resume-matcher.git
cd resume-matcher

Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

Install dependencies:
pip install -r requirements.txt

Download spaCy English model:
python -m spacy download en_core_web_sm

Usage
Run the main script:
python main.py
You will be prompted to select a resume and a job description from the data/ folder.

Alternatively, you can pass file paths directly:
python main.py --resume data/resumes/resume1.txt --job data/job_descriptions/jd1.txt

Example Output
=== Resume Match Result ===
Resume: data/resumes/resume1.txt
Job Description: data/job_descriptions/jd1.txt
TF-IDF Match Score: 28.42%
Semantic Match Score: 64.81%
Skill Match Score: 50.00%
Skills Matched: ['excel', 'python', 'power bi']
Skills Missing: ['docker', 'aws', 'git']
===========================

Adding New Resumes or Job Descriptions
Place new resume files in data/resumes/ (PDF or TXT).

Place new job descriptions in data/job_descriptions/ (TXT).

Run the matcher as usual to test new combinations.

Future Enhancements
Batch processing for multiple resumes at once.

Build a Streamlit or web interface for drag-and-drop resume upload.

Weighted scoring combining TF-IDF, semantic, and skill matches.

Improved skill extraction using NER for certifications, tools, and frameworks.

Requirements
Python 3.10+

Dependencies: See requirements.txt

License
This project is licensed under the MIT License.
