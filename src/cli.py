import argparse
from .matcher import match_resume_to_job

def run_cli():
    parser = argparse.ArgumentParser(description="Resume Matcher CLI")
    parser.add_argument("--resume", required=True, help="Path to resume file (PDF/TXT)")
    parser.add_argument("--job", required=True, help="Path to job description file (TXT)")

    args = parser.parse_args()

    result = match_resume_to_job(args.resume, args.job)
    print("\n=== Resume Match Result ===")
    print(f"Resume: {result['resume']}")
    print(f"Job Description: {result['job_description']}")
    print(f"Match Score: {result['match_score']}%")
    print(f"Skills Matched: {', '.join(result['skills_matched'])}")
    print(f"Skills Missing: {', '.join(result['skills_missing'])}")
    print("===========================\n")
