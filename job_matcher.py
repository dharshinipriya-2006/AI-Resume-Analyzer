def calculate_match(resume_skills, job_skills):

    matched_skills = []

    for skill in job_skills:

        if skill.lower() in [s.lower() for s in resume_skills]:
            matched_skills.append(skill)

    if len(job_skills) == 0:
        match_percentage = 0
    else:
        match_percentage = (
            len(matched_skills) / len(job_skills)
        ) * 100

    missing_skills = [
        skill for skill in job_skills
        if skill not in matched_skills
    ]

    return matched_skills, missing_skills, match_percentage
