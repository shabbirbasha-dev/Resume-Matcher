# main.py
import os
from src.pdf_utils import extract_text_from_pdf
from src.nlp_utils import (
    extract_skills_refined,
    extract_skills_from_jd,
    compute_skill_overlap_dynamic,
    compute_tfidf_similarity,
    compute_semantic_similarity,
    TECH_SKILLS
)

def select_file(folder, file_types):
    """
    List files in folder and let the user select one by number.
    """
    files = [f for f in os.listdir(folder) if f.lower().endswith(file_types)]
    if not files:
        print(f"No files found in {folder}")
        return None

    print(f"\nAvailable files in '{folder}':")
    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")

    while True:
        try:
            choice = int(input("Select file number: "))
            if 1 <= choice <= len(files):
                return os.path.join(folder, files[choice - 1])
            else:
                print(f"Please enter a number between 1 and {len(files)}")
        except ValueError:
            print("Invalid input. Enter a number.")

def read_file(path):
    """
    Read PDF or TXT file and return text.
    """
    if path.lower().endswith(".pdf"):
        return extract_text_from_pdf(path)
    else:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

def main():
    print("=== Resume Matcher Interactive CLI ===")

    resume_folder = "data/resumes/"
    jd_folder = "data/job_descriptions/"

    # --- Select resume ---
    resume_path = select_file(resume_folder, (".txt", ".pdf"))
    if not resume_path:
        return
    resume_text = read_file(resume_path)

    # --- Select job description ---
    jd_path = select_file(jd_folder, (".txt",))
    if not jd_path:
        return
    jd_text = read_file(jd_path)

    # --- Extract skills ---
    resume_skills = extract_skills_refined(resume_text)
    jd_skills = extract_skills_from_jd(jd_text, master_skills=TECH_SKILLS)

    # --- Compute skill overlap ---
    skill_score, matched_skills, missing_skills = compute_skill_overlap_dynamic(resume_skills, jd_skills)

    # --- Compute TF-IDF and Semantic similarity ---
    tfidf_score = compute_tfidf_similarity(resume_text, jd_text)
    semantic_score = compute_semantic_similarity(resume_text, jd_text)

    # --- Display results ---
    print("\n=== Resume Match Result ===")
    print(f"Resume: {resume_path}")
    print(f"Job Description: {jd_path}")
    print(f"TF-IDF Match Score: {tfidf_score:.2f}%")
    print(f"Semantic Match Score: {semantic_score:.2f}%")
    print(f"Skill Match Score: {skill_score:.2f}%")
    print(f"Skills Matched: {matched_skills}")
    print(f"Skills Missing: {missing_skills}")
    print("===========================\n")


if __name__ == "__main__":
    main()
