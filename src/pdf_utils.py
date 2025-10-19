# pdf_utils.py (or at the top of main.py)
import re
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """
    Extracts and cleans text from a PDF file for resume matching.
    """
    reader = PdfReader(pdf_path)
    raw_text = ""
    for page in reader.pages:
        raw_text += page.extract_text() + "\n"

    # --- CLEANING ---
    # Remove invisible characters
    clean_text = raw_text.replace("\u200B", "")
    clean_text = clean_text.replace("\xa0", " ")  # non-breaking spaces

    # Replace multiple spaces, tabs, newlines with a single space
    clean_text = re.sub(r"\s+", " ", clean_text)

    # Strip leading/trailing spaces
    clean_text = clean_text.strip()

    return clean_text
