import re

def extract_skills(resume_text):

    skills = [
        "Python",
        "Java",
        "C++",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",
        "AWS",
        "Azure",
        "Google Cloud",
        "Docker",
        "Kubernetes",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Flask",
        "Django",
        "TensorFlow",
        "Scikit-learn"
    ]

    found_skills = []

    text = resume_text.lower()

    for skill in skills:
        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills
