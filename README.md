# 🤖 AI-Powered Resume Screening Tool

An intelligent resume screening web app that helps HR teams, recruiters, and startups automatically rank candidates based on their skills compared to a job description.

---

## 🚀 Features

- Upload multiple resumes in **PDF or DOCX** format  
- Extract skills from resumes using **NLP (SpaCy)**  
- Extract required skills from a **Job Description**  
- Compare resumes against the job description and **rank candidates**  
- Show **matched and missing skills** for each candidate  
- Visualize candidate match percentages with **interactive bar charts**  
- Show overall **skills coverage** across all resumes  
- Export results as **CSV** or **Excel**  
- Highlight the **top candidate** automatically  

---

## 🛠 Tech Stack

- **Python**  
- **Streamlit** for interactive web app  
- **Pandas** for data processing  
- **SpaCy** for NLP skill extraction  
- **Altair** for charts and visualization  
- **Python-Docx** and **PyMuPDF** for parsing resumes  
- **OpenPyXL** for Excel export  

---

## 📁 Project Structure

AI-Resume-Screener/
├── app.py # Streamlit web app
├── matcher.py # Resume scoring and ranking logic
├── resume_parser.py # Extract resume text
├── jd_parser.py # Extract skills from job description
├── resumes/ # Sample resumes (PDF/DOCX)
├── requirements.txt # Python dependencies
└── README.md

---

## ⚡ How to Run Locally

1. Clone the repo:

'''bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Screener.git
cd AI-Resume-Screener'''

2. (Optional but recommended) Create a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3. install dependencies
   pip install -r requirements.txt
4. run the streamlit app
   streamlite run app.py

📝 Notes

Works with Python 3.9+

Make sure required packages (spacy, pandas, streamlit, altair, python-docx, PyMuPDF, openpyxl) are installed

This project can be deployed on Streamlit Cloud, Heroku, or AWS for sharing online
<img width="1754" height="633" alt="Screenshot 2025-09-06 175321" src="https://github.com/user-attachments/assets/3bf8ee48-472d-4c74-93cc-e0adfc2264df" />
<img width="1842" height="730" alt="Screenshot 2025-09-06 175308" src="https://github.com/user-attachments/assets/fe12685e-923b-4be7-b00c-d9663bea44a2" />
<img width="1765" height="403" alt="Screenshot 2025-09-06 175252" src="https://github.com/user-attachments/assets/b943a137-65c6-40f2-8d7c-178563b70275" />
