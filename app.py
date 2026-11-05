import streamlit as st
import PyPDF2

from skill_extractor import extract_skills
from job_matcher import calculate_match

st.title("AI Resume Analyzer & Job Matcher")

st.write("Analyze your resume and match it with job requirements.")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if uploaded_file is not None:

    reader = PyPDF2.PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        resume_text += page.extract_text() or ""

    st.subheader("Extracted Resume Skills")

    resume_skills = extract_skills(resume_text)

    st.write(resume_skills)

    if st.button("Analyze Resume"):

        if not job_description.strip():
            st.warning("Please enter a job description.")

        else:

            job_skills = extract_skills(job_description)

            matched, missing, percentage = calculate_match(
                resume_skills,
                job_skills
            )

            st.subheader("Job Matching Results")

            st.metric(
                "Resume Match Percentage",
                f"{percentage:.2f}%"
            )

            st.write("### Matching Skills")
            st.success(", ".join(matched) if matched else "No matching skills found.")

            st.write("### Missing Skills")
            st.warning(", ".join(missing) if missing else "No missing skills!")
