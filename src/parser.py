import pdfplumber

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_text_from_file(file_path):
    if file_path.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith(".txt"):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        raise ValueError("Unsupported file format. Use .pdf or .txt")

def extract_relevant_section(text):
    sections = ["skills", "technical skills", "experience", "projects"]
    text_lower = text.lower()
    for section in sections:
        if section in text_lower:
            start = text_lower.find(section)
            return text[start:]
    return text  # fallback
