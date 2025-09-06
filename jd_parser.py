import spacy

# Try to load SpaCy model (if not available, fallback to keywords)
try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = None
    print("[WARNING] SpaCy model not found. Falling back to keyword matching.")


# Define a list of common tech skills (extend as needed)
COMMON_SKILLS = [
    "python", "java", "c++", "sql", "excel", "power bi",
    "machine learning", "deep learning", "nlp", "spacy",
    "tensorflow", "pytorch", "flask", "django", "react",
    "javascript", "html", "css", "data analysis", "pandas", "numpy"
]


def extract_skills_from_jd(jd_text: str):
    """
    Extracts skills from a job description using SpaCy NER if available,
    otherwise uses keyword matching.
    """
    jd_text_lower = jd_text.lower()
    found_skills = set()

    if nlp:
        doc = nlp(jd_text)
        # Named Entity Recognition (NER) + keyword match
        for token in doc:
            if token.text.lower() in COMMON_SKILLS:
                found_skills.add(token.text.lower())

    # Keyword-based matching (fallback)
    for skill in COMMON_SKILLS:
        if skill in jd_text_lower:
            found_skills.add(skill)

    return list(found_skills)
