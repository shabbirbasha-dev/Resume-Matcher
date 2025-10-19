import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import spacy
from collections import Counter

nltk.download("stopwords")
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words("english"))
MODEL = SentenceTransformer('all-MiniLM-L6-v2')
NLP = spacy.load("en_core_web_sm")

# Master technical skill list (expandable)
TECH_SKILLS = [
    "python", "sql", "excel", "power bi", "tableau", "pandas", "numpy",
    "javascript", "react", "node.js", "docker", "aws", "mysql", "mongodb",
    "html", "css", "tensorflow", "keras", "git", "ci/cd", "rest api", "linux",
    "c++", "java", "php", "laravel", "angular", "vue.js", "typescript", "next.js",
    "redux", "graphql", "webpack", "jest", "mocha"
]

def normalize_skill_text(text):
    """
    Normalize text for skill matching with better handling of special characters
    """
    text = text.lower()
    # Replace multiple spaces with single space
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    tokens = [word for word in text.split() if word not in STOPWORDS]
    return " ".join(tokens)

def compute_tfidf_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100

def compute_semantic_similarity(text1, text2):
    embeddings = MODEL.encode([text1, text2])
    return cosine_similarity([embeddings[0]], [embeddings[1]])[0][0] * 100

def extract_skills_refined(text):
    """
    Extract technical skills from resume using robust matching.
    Handles multi-word skills like CI/CD, REST API, Node.js.
    """
    text_norm = normalize_skill_text(text)
    matched_skills = []

    for skill in TECH_SKILLS:
        skill_lower = skill.lower()
        
        # Handle special characters in skills
        if '/' in skill_lower or '+' in skill_lower or '.' in skill_lower:
            # For skills with special chars like CI/CD, C++, Node.js
            # Create a flexible pattern that handles spaces and variations
            skill_pattern = r'\b' + re.escape(skill_lower) + r'\b'
            skill_pattern = skill_pattern.replace(r'\/', r'[\/\s]*')  # Handle CI/CD or CI CD
            skill_pattern = skill_pattern.replace(r'\.', r'[\.\s]*')  # Handle Node.js or Node js
            skill_pattern = skill_pattern.replace(r'\+', r'[\+\s]*')  # Handle C++ or C+ +
        else:
            # For regular skills
            skill_pattern = r'\b' + re.escape(skill_lower) + r'\b'
        
        if re.search(skill_pattern, text_norm, flags=re.IGNORECASE):
            matched_skills.append(skill)
        else:
            # Additional check for common variations
            variations = {
                "ci/cd": ["ci cd", "ci  cd", "continuous integration", "continuous deployment"],
                "rest api": ["restapi", "restful api"],
                "node.js": ["node js", "nodejs"],
                "c++": ["c plus plus", "cpp"],
                "power bi": ["powerbi"]
            }
            
            if skill_lower in variations:
                for variation in variations[skill_lower]:
                    if variation in text_norm:
                        matched_skills.append(skill)
                        break

    return list(set(matched_skills))

def extract_skills_from_jd(jd_text, master_skills=None):
    """
    Hybrid approach: extract known skills + discover new ones from JD
    """
    jd_text_norm = normalize_skill_text(jd_text)
    
    # Method 1: Extract using master skills pattern matching
    known_skills = extract_skills_refined(jd_text)
    
    # Method 2: Extract new skills using NLP
    doc = NLP(jd_text_norm)
    skill_candidates = [chunk.text.strip() for chunk in doc.noun_chunks if len(chunk.text.split()) <= 3]
    skill_candidates += [ent.text.strip() for ent in doc.ents if ent.label_ in ["ORG","PRODUCT","WORK_OF_ART","LANGUAGE","NORP"]]
    
    # Normalize and filter new skills
    new_skills = []
    for skill in skill_candidates:
        normalized = normalize_skill_text(skill)
        if (len(normalized) >= 2 and 
            normalized not in STOPWORDS and 
            normalized not in [normalize_skill_text(s) for s in known_skills]):
            new_skills.append(normalized)
    
    # Combine both approaches
    all_skills = known_skills + list(set(new_skills))
    
    # Optional: Filter by master_skills if you want to restrict to known tech skills
    if master_skills:
        normalized_master = [normalize_skill_text(s) for s in master_skills]
        all_skills = [skill for skill in all_skills if normalize_skill_text(skill) in normalized_master]
    
    return all_skills

def compute_skill_overlap_dynamic(resume_skills, jd_skills):
    if not jd_skills:
        return 0, [], []
    matched = set(resume_skills).intersection(set(jd_skills))
    missing = set(jd_skills) - set(resume_skills)
    score = len(matched) / len(jd_skills) * 100
    return score, list(matched), list(missing)

# Test the function with CI/CD
def test_ci_cd_matching():
    test_cases = [
        "I have experience with CI/CD pipelines",
        "Worked on ci cd implementation",
        "Knowledge of continuous integration and deployment",
        "CI CD Jenkins pipeline",
        "ci/cd tools like jenkins",
        "continuous integration continuous deployment"
    ]
    
    for test in test_cases:
        skills = extract_skills_refined(test)
        print(f"Text: {test}")
        print(f"Matched skills: {skills}")
        print("---")

# Uncomment to test
# test_ci_cd_matching()