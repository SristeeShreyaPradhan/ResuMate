
from analyzer import analyze_score,plot_skill_match

def main():
    print("\n RESUME ANALYZER & JOB FIT SCORE CALCULATOR")

    resume_path = "C:\\Users\\Administrator\\Python\\sample_data\\resume_sample.txt"
    jd_path = "C:\\Users\\Administrator\\Python\\sample_data\\job_description_sample.txt"
    soft_skills_path= "C:\\Users\\Administrator\\Python\\key_words\\soft_skills.txt"
    tech_skills_path = "C:\\Users\\Administrator\\Python\\key_words\\technical_skills.txt"

    results = analyze_score(resume_path, jd_path, tech_skills_path, soft_skills_path)

    print("\n============================")
    print(f"Technical Fit Score: {results['tech_score']}%")
    print("============================")
    print(f"Matched Technical Skills ({len(results['matched_tech'])}): {', '.join(results['matched_tech'])}")
    print(f"Missing Technical Skills ({len(results['missing_tech'])}): {', '.join(results['missing_tech'])}")
    print(f"Extra Technical Skills ({len(results['extra_tech'])}): {', '.join(results['extra_tech'])}")

    print("\n============================")
    print(f"Soft Skills Fit Score: {results['soft_score']}%")
    print("============================")
    print(f"Matched Soft Skills ({len(results['matched_soft'])}): {', '.join(results['matched_soft'])}")
    print(f"Missing Soft Skills ({len(results['missing_soft'])}): {', '.join(results['missing_soft'])}")
    print(f"Extra Soft Skills ({len(results['extra_soft'])}): {', '.join(results['extra_soft'])}")
    total_score= (results['tech_score']+results['soft_score'])/2
    total_round_score= round(total_score)
    print(f"Job Fit Score: {total_round_score} %")

    plot_skill_match(results) 

if __name__ == "__main__":
    main()