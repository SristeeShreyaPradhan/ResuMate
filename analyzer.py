
import re
import matplotlib.pyplot as plt

def load_file(filepath):
    #Reads a text file and returns text in lowercase
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read().lower()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return ""



def extract_skills(resume, skills_file):
    found_skills = []
    # Tokenize resume into a set of words
    resume_words = set(re.findall(r'\w+', resume.lower()))
    
    for skill in skills_file:
        skill_words = skill.lower().split()
        # Check if all words in the skill are present in resume words
        if all(word in resume_words for word in skill_words):
            found_skills.append(skill)
    return found_skills


def load_keywords(filepath):
   #Loads keywords from a file
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return [line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Skill list file not found: {filepath}")
        return []

#Job skills score calculator:

def analyze_score(resume_sample,job_description_sample ,technical_skills, soft_skills):
    resume_text = load_file(resume_sample)
    jd_text = load_file(job_description_sample)

    tech_keywords = load_keywords(technical_skills)
    soft_keywords = load_keywords(soft_skills)

    # Extracting skills
    resume_tech = set(extract_skills(resume_text, tech_keywords))
    jd_tech = set(extract_skills(jd_text, tech_keywords))

    resume_soft = set(extract_skills(resume_text, soft_keywords))
    jd_soft = set(extract_skills(jd_text, soft_keywords))

    # Technical skills comparison
    matched_tech = resume_tech & jd_tech
    missing_tech = jd_tech - resume_tech
    extra_tech = resume_tech - jd_tech

    # Soft skills comparison
    matched_soft = resume_soft & jd_soft
    missing_soft = jd_soft - resume_soft
    extra_soft = resume_soft - jd_soft

    score_tech = int((len(matched_tech) / len(jd_tech)) * 100) if jd_tech else 0
    score_soft = int((len(matched_soft) / len(jd_soft)) * 100) if jd_soft else 0

    return {
        "tech_score": score_tech,
        "soft_score": score_soft,
        "matched_tech": sorted(matched_tech),
        "missing_tech": sorted(missing_tech),
        "extra_tech": sorted(extra_tech),
        "matched_soft": sorted(matched_soft),
        "missing_soft": sorted(missing_soft),
        "extra_soft": sorted(extra_soft),
    }



def plot_skill_match(results):
     
    categories = ['Matched', 'Missing', 'Extra']

    tech_matches = [
        len(results['matched_tech']),
        len(results['missing_tech']),
        len(results['extra_tech'])
    ]

    soft_matches = [
        len(results['matched_soft']),
        len(results['missing_soft']),
        len(results['extra_soft'])
    ]

    colors = ['#47B39C', '#EC6B56', '#FFC154']  

    # Technical Skills Pie Chart
    plt.pie(tech_matches, labels=categories, autopct='%1.0f%%', colors=colors)
    plt.title('Technical Skills')
    plt.show()

    # Soft Skills Pie Chart
    plt.pie(soft_matches, labels=categories, autopct='%1.0f%%', colors=colors)
    plt.title('Soft Skills')
    plt.show()
