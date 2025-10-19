# Resume-Matcher

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![NLP](https://img.shields.io/badge/NLP-SpaCy%2BTransformers-orange)](https://spacy.io)

A **Python-based Resume Matcher** that evaluates how well a candidate's resume fits a job description using **NLP, TF-IDF, Semantic Similarity, and Skill Extraction**.  
Supports **PDF and TXT resumes**, dynamic skill matching, and an **interactive CLI**.

---

## 🚀 Features

- **🤖 AI-Powered Matching** - Combines TF-IDF and semantic similarity for accurate results
- **🔧 Skill Extraction** - Automatically detects technical skills from resumes and job descriptions
- **📄 Multi-Format Support** - Handles PDF and text resume formats
- **⚡ Complex Skill Recognition** - Identifies skills like CI/CD, REST API, Node.js, C++
- **💬 Interactive CLI** - Easy-to-use command line interface
- **📊 Detailed Analytics** - Skill overlap, missing skills, and multiple scoring metrics

---

## 📁 Project Structure
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
│ ├── cli.py # Command-line interface
│ ├── matcher.py # Core matching algorithms
│ ├── nlp_utils.py # NLP processing utilities
│ ├── parser.py # Resume/JD parsing
│ └── pdf_utils.py # PDF processing
│
├── main.py # Main application entry point
├── requirements.txt # Dependencies
├── LICENSE
└── README.md

---

## 🛠 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step-by-Step Setup

1. **Clone the repository**
   
   
#### Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

#### Install dependencies
```bash
pip install -r requirements.txt
```

#### Download NLP model
```bash
python -c "import nltk; nltk.download('stopwords')"
python -m spacy download en_core_web_sm
```

## 📖 Usage

### Interactive Mode
```bash
python main.py
```
You'll be prompted to select a resume and job description from the data/ folder.

### Direct File Mode
```bash
python main.py --resume data/resumes/resume1.txt --job data/job_descriptions/jd1.txt
```

### Python API
```python
from src.matcher import ResumeMatcher

matcher = ResumeMatcher()
results = matcher.match("resume.pdf", "job_description.txt")
print(f"Overall Match: {results['score']}%")
```

## 📊 Example Output
```text
=== Resume Match Result ===
📄 Resume: data/resumes/resume1.txt
📋 Job Description: data/job_descriptions/jd1.txt

🎯 Match Scores:
   • TF-IDF Similarity: 28.42%
   • Semantic Similarity: 64.81%
   • Skill Match: 50.00%

✅ Skills Matched: ['python', 'excel', 'power bi']
❌ Skills Missing: ['docker', 'aws', 'git']
===========================
```

## ➕ Adding Content

### Adding Resumes
Place resume files in data/resumes/

Supported formats: PDF, TXT

File naming: resume_{name}.pdf or resume_{name}.txt

### Adding Job Descriptions
Place JD files in data/job_descriptions/

Format: TXT files

File naming: jd_{company}.txt

## 🚧 Future Enhancements

Batch Processing - Analyze multiple resumes at once

Web Interface - Streamlit or Flask-based UI

Weighted Scoring - Customizable scoring weights

Enhanced Skill DB - Expanded technical skills library

Export Reports - PDF/Excel result reports

API Endpoints - REST API for integration

## 🛠 Requirements
Python 3.8+

Dependencies listed in requirements.txt

## 🤝 Contributing
We welcome contributions! Please feel free to submit pull requests or open issues for bugs and feature requests.

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author
Shabbir Basha

GitHub: @shabbirbasha-dev
