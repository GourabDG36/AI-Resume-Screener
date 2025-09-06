import streamlit as st
import pandas as pd
import os
import tempfile
from matcher import rank_resumes
import altair as alt
import io
from openpyxl import Workbook

st.set_page_config(page_title="AI Resume Screener", layout="wide")

st.title("🤖 AI-Powered Resume Screening Tool")
st.write("Upload resumes and a job description to rank candidates automatically.")

# --- Upload Job Description ---
st.subheader("📄 Job Description")
job_description = st.text_area("Paste the job description here", height=200)

# --- Upload Resumes ---
st.subheader("📂 Upload Resumes (PDF/DOCX)")
uploaded_files = st.file_uploader("Upload multiple resumes", type=["pdf", "docx"], accept_multiple_files=True)

# ✅ Process Resumes Button
if st.button("Process Resumes"):
    if not job_description:
        st.error("Please paste a job description.")
    elif not uploaded_files:
        st.error("Please upload at least one resume.")
    else:
        with st.spinner("Processing resumes..."):
            # Save uploaded resumes temporarily
            with tempfile.TemporaryDirectory() as tempdir:
                for uploaded_file in uploaded_files:
                    save_path = os.path.join(tempdir, uploaded_file.name)
                    with open(save_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())

                # Run ranking
                results = rank_resumes(tempdir, job_description)

            # 🔽 Convert results to DataFrame
            df = pd.DataFrame(results)

            # --- Candidate Ranking Display ---
            st.subheader("🏆 Candidate Ranking")
            for res in results:
                st.markdown(f"""
                **{res['name']}**
                - ✅ Score: **{res['score']}**
                - 📊 Match: **{res['percentage']}%**
                - 🟢 Matched Skills: {', '.join(res['matched']) if res['matched'] else 'None'}
                - 🔴 Missing Skills: {', '.join(res['missing']) if res['missing'] else 'None'}
                ---
                """)

            # --- CSV Export ---
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Results as CSV",
                data=csv,
                file_name="candidate_ranking.csv",
                mime="text/csv",
            )

            # --- Candidate Scores Chart ---
            st.subheader("📊 Candidate Match Percentage")
            chart = (
                alt.Chart(df)
                .mark_bar()
                .encode(
                    x=alt.X("name", sort="-y"),
                    y="percentage",
                    tooltip=["name", "score", "percentage"]
                )
            )
            st.altair_chart(chart, use_container_width=True)

            # --- Highlight Best Candidate ---
            best_candidate = df.iloc[0]
            st.success(f"🏆 Best Candidate: {best_candidate['name']} "
                       f"with {best_candidate['percentage']}% match!")

            # --- Skills Coverage ---
            all_skills = []
            for res in results:
                all_skills.extend(res['matched'])

            skill_counts = pd.Series(all_skills).value_counts().reset_index()
            skill_counts.columns = ["skill", "count"]

            st.subheader("🧾 Overall Skills Coverage")
            st.bar_chart(skill_counts.set_index("skill"))

            # --- Excel Export with Multiple Sheets ---
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                df.to_excel(writer, index=False, sheet_name="Ranking")
                skill_counts.to_excel(writer, index=False, sheet_name="Skills Coverage")

            st.download_button(
                label="📥 Download Results as Excel",
                data=output.getvalue(),
                file_name="candidate_ranking.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
