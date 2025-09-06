import fitz  # PyMuPDF
import docx2txt
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(docx_path):
    return docx2txt.process(docx_path)

def extract_text_from_file(file_path):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        return ""
    
def extract_resumes_from_folder(folder_path):
    resumes = {}
    for filename in os.listdir(folder_path):
        if filename.endswith((".pdf", ".docx")):
            full_path = os.path.join(folder_path, filename)
            resumes[filename] = extract_text_from_file(full_path)
    return resumes

from resume_parser import extract_resumes_from_folder

resumes = extract_resumes_from_folder("resumes/")
for name, text in resumes.items():
    print(f"--- {name} ---\n{text[:300]}...\n")
