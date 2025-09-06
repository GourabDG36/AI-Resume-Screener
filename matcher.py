from resume_parser import extract_resumes_from_folder
from jd_parser import extract_skills_from_jd

def score_resume(resume_text: str, jd_skills: list):
    """
    Returns both the match score and matched/missing skills.
    """
    resume_text_lower = resume_text.lower()
    matched = [skill for skill in jd_skills if skill in resume_text_lower]
    missing = [skill for skill in jd_skills if skill not in resume_text_lower]
    score = len(matched)
    return score, matched, missing


def rank_resumes(resume_folder: str, job_description: str):
    resumes = extract_resumes_from_folder(resume_folder)
    jd_skills = extract_skills_from_jd(job_description)

    results = []
    for name, text in resumes.items():
        score, matched, missing = score_resume(text, jd_skills)
        results.append({
            "name": name,
            "score": score,
            "matched": matched,
            "missing": missing,
            "percentage": round((score / len(jd_skills)) * 100, 2) if jd_skills else 0
        })

    # Sort by score (descending)
    results.sort(key=lambda x: x["score"], reverse=True)
    return results
