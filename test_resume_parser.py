from resume_parser import extract_resumes_from_folder

# Path to your resumes folder
resumes = extract_resumes_from_folder("resumes/")

# Print first 300 characters of each resume
for name, text in resumes.items():
    print(f"--- {name} ---")
    print(text[:300], "...\n")
