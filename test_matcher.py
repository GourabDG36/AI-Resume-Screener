from matcher import rank_resumes

job_description = """
We are looking for a Data Scientist with skills in Python, SQL, Machine Learning,
and Data Analysis. Knowledge of TensorFlow and NLP is preferred.
"""

results = rank_resumes("resumes/", job_description)

print("Candidate Ranking:")
for res in results:
    print(f"{res['name']} → Score: {res['score']}, {res['percentage']}% match")
    print(f"Matched: {res['matched']}")
    print(f"Missing: {res['missing']}\n")
