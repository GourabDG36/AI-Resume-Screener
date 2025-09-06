from jd_parser import extract_skills_from_jd

job_description = """
We are looking for a Data Scientist with strong skills in Python, SQL, 
Machine Learning, and Data Analysis. Experience with TensorFlow and NLP is a plus.
"""

skills = extract_skills_from_jd(job_description)
print("Extracted Skills:", skills)
