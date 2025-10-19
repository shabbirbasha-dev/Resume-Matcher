from .parser import extract_text_from_file, extract_relevant_section
from .nlp_utils import preprocess_text, compute_tfidf_similarity, compute_semantic_similarity
from .nlp_utils import extract_skills_refined, extract_skills_from_jd, compute_skill_overlap_dynamic, TECH_SKILLS

def match_resume_to_job(resume_path, job_path):
    resume_text = extract_text_from_file(resume_path)
    job_text = extract_text_from_file(job_path)

    # Extract relevant sections
    resume_text = extract_relevant_section(resume_text)
    job_text = extract_relevant_section(job_text)

    # Preprocess for TF-IDF / semantic similarity
    resume_clean = preprocess_text(resume_text)
    job_clean = preprocess_text(job_text)

    # TF-IDF similarity
    tfidf_score = compute_tfidf_similarity(resume_clean, job_clean)

    # Semantic similarity
    semantic_score = compute_semantic_similarity(resume_clean, job_clean)

    # Refined resume skills
    resume_skills = extract_skills_refined(resume_text)

    # Dynamic JD skills
    jd_skills = extract_skills_from_jd(job_text, master_skills=TECH_SKILLS)

    # Compute skill overlap
    skill_score, skills_matched, skills_missing = compute_skill_overlap_dynamic(resume_skills, jd_skills)

    # Weighted final score
    final_score = 0.4 * skill_score + 0.3 * semantic_score + 0.3 * tfidf_score

    return {
        "resume": resume_path,
        "job_description": job_path,
        "match_score": round(final_score,2),
        "skills_matched": skills_matched,
        "skills_missing": skills_missing
    }
