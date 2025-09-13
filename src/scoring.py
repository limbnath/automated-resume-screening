from src.skills import extract_skills_fuzzy
import re

def extract_years_experience(text: str):
    # naive regex: look for patterns like '3 years', '2 yrs', '5+ years'
    m = re.findall(r'(\d+)\s*\+?\s*(?:years|year|yrs|yr)', text.lower())
    if m:
        try:
            return max(int(x) for x in m)
        except:
            return 0
    return 0

def compute_score(resume_text: str, jd_text: str, required_skills_list=None):
    resume_skills = set(extract_skills_fuzzy(resume_text))
    jd_skills = set(extract_skills_fuzzy(jd_text))
    if required_skills_list:
        jd_skills = set([s.lower() for s in required_skills_list])

    matched = resume_skills.intersection(jd_skills)
    matched_count = len(matched)
    jd_count = max(len(jd_skills), 1)

    skill_match_score = (matched_count / jd_count) * 80
    keywords_score = (matched_count / jd_count) * 10

    years = extract_years_experience(resume_text)
    experience_score = min(years, 5) / 5 * 10  # cap at 5 years for score

    final_score = skill_match_score + keywords_score + experience_score
    return {
        "resume_skills": sorted(list(resume_skills)),
        "jd_skills": sorted(list(jd_skills)),
        "matched_skills": sorted(list(matched)),
        "score": round(final_score, 2)
    }
