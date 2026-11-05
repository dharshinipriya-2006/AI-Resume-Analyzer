import streamlit as st
import PyPDF2

from skill_extractor import extract_skills
from job_matcher import calculate_match

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("AI Resume Analyzer & Job Matcher")

st.write(
    "Analyze your resume, identify technical skills "
    "and discover your job compatibility."
)

st.divider()

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=180
)

if st.button("Analyze Resume", type="primary"):

    if uploaded_file is None:
        st.warning("Please upload your resume.")

    elif not job_description.strip():
        st.warning("Please enter a job description.")

    else:
        try:
            reader = PyPDF2.PdfReader(uploaded_file)

            resume_text = ""

            for page in reader.pages:
                resume_text += page.extract_text() or ""

            if not resume_text.strip():
                st.error("No readable text found in this PDF.")
                st.stop()

            resume_skills = extract_skills(resume_text)
            job_skills = extract_skills(job_description)

            matched, missing, percentage = calculate_match(
                resume_skills,
                job_skills
            )

            st.divider()

            st.header("Analysis Results")

            col1, col2, col3 = st.columns(3)

            col1.metric("Match Score", f"{percentage:.2f}%")
            col2.metric("Matching Skills", len(matched))
            col3.metric("Missing Skills", len(missing))

            st.subheader("Job Compatibility")

            st.progress(int(percentage))

            st.subheader("Matching Skills")

            if matched:
                st.success(", ".join(matched))
            else:
                st.info("No matching skills found.")

            st.subheader("Missing Skills")

            if missing:
                st.warning(", ".join(missing))
            else:
                st.success("You have all the detected required skills!")

            st.subheader("Skill Improvement Recommendations")

            if missing:
                for skill in missing:
                    st.write(f"📚 Learn {skill}")
            else:
                st.write("Continue improving your technical skills.")

            with st.expander("View Extracted Resume Text"):
                st.write(resume_text)

        except Exception as e:
            st.error(f"Error analyzing resume: {e}")
