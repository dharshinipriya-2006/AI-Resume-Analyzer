import streamlit as st
import PyPDF2
from skill_extractor import extract_skills

st.title("AI Resume Analyzer")

st.write("Upload your resume to analyze your technical skills.")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    reader = PyPDF2.PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        resume_text += page.extract_text() or ""

    st.subheader("Extracted Resume Text")
    st.write(resume_text)

    skills = extract_skills(resume_text)

    st.subheader("Detected Technical Skills")

    if skills:
        for skill in skills:
            st.success(skill)
    else:
        st.warning("No technical skills detected.")
