
def job_portal():

    print("\n========== JOB RECOMMENDATION SYSTEM ==========")

    # ---------------- USER INPUT ----------------
    user_role = input("Enter your role: ").lower().strip()

    user_skills = input("Enter your skills (comma separated): ").lower().split(",")
    user_skills = set([skill.strip() for skill in user_skills])

    # ---------------- ROLE-SKILL REFERENCE ----------------
    role_skill_reference = {
        "java developer": {"java", "spring", "hibernate", "sql"},
        "python developer": {"python", "django", "flask", "sql"},
        "data analyst": {"excel", "sql", "power bi", "tableau", "data visualization"},
        "data scientist": {"python", "machine learning","numpy", "statistics"},
        "data engineer": {"python", "sql", "spark", "hadoop", "etl", "aws"},
        "ml engineer": {"python", "machine learning", "tensorflow", "pytorch"}
    }

    # ---------------- JOB DATABASE ----------------
    jobs = [
        {"company": "Vbha", "role": "java developer", "skills": {"java", "spring", "sql"}},
        {"company": "HSBC", "role": "data analyst", "skills": {"python", "excel", "sql", "power bi"}},  # wrong

        {"company": "Google", "role": "data scientist", "skills": {"python", "machine learning", "pandas"}},
        {"company": "Amazon", "role": "data engineer", "skills": {"python", "sql", "spark", "aws"}},
        {"company": "Microsoft", "role": "data analyst", "skills": {"excel", "sql", "power bi"}},
        {"company": "Meta", "role": "ml engineer", "skills": {"python", "machine learning", "tensorflow"}},

        {"company": "FakeData Inc", "role": "data scientist", "skills": {"excel", "power bi"}}  # wrong
    ]

    primary_jobs = []
    related_jobs = []

    print("\n--- JOB RESULTS ---\n")

    for job in jobs:

        job_role = job["role"]
        job_skills = set([skill.lower() for skill in job["skills"]])  # normalize

        # ---------------- STEP 1: VALIDATION ----------------
        reference_skills = role_skill_reference.get(job_role, set())

        if len(job_skills) == 0:
            continue

        common_skills = job_skills.intersection(reference_skills)
        validation_score = len(common_skills) / len(job_skills)

        # remove wrong company data
        if validation_score < 0.3:
            continue

        # ---------------- STEP 2: USER MATCH ----------------
        matched_skills = user_skills.intersection(job_skills)

        if len(matched_skills) == 0:
            continue
        
        match_percentage = (
            len(matched_skills) / len(job_skills)
        ) * 100

        # ---------------- MATCH LEVEL ----------------
        if match_percentage >= 70:
            level = "Strong Match"
        elif match_percentage >= 40:
            level = "Moderate Match"
        else:
            level = "Weak Match"

        missing_skills = job_skills - user_skills


        job_result = {
            "company": job["company"],
            "role": job_role,
            "matched": len(matched_skills),
            "total": len(job_skills),
            "score": round(match_percentage, 2),
            "level": level,
            "missing": missing_skills
        }

        # ---------------- ROLE-FIRST LOGIC ----------------
        if job_role == user_role:
            primary_jobs.append(job_result)
        else:
            related_jobs.append(job_result)

    # ---------------- SORT ----------------
    primary_jobs.sort(key=lambda x: x["score"], reverse=True)
    related_jobs.sort(key=lambda x: x["score"], reverse=True)

    # ---------------- OUTPUT ----------------
    if not primary_jobs and not related_jobs:
        print("\nNo matching jobs found")
        return

    print("\n===== PRIMARY JOBS ======\n")

    if primary_jobs:
        for r in primary_jobs:
            print("Company:", r["company"])
            print("Role:", r["role"])
            print("Matched Skills:", r["matched"], "/", r["total"])
            print("Match %:", round(r["score"], 2))
            print("Match Level:", r["level"])
            print("Missing Skills:", ", ".join(job["missing"]))
            print("---------------------")
    else:
        print("No jobs available for your role.\n")

    print("\n====== RELATED JOBS =====\n")

    if related_jobs:

        for r in related_jobs:
            print("Company:", r["company"])
            print("Role:", r["role"])
            print("Matched Skills:", r["matched"], "/", r["total"])
            print("Match %:", round(r["score"], "%"))
            print("Match Level:", r["level"])
            print("Missing Skills:", ", ".join(job["missing"]))
            print("---------------------")
    
    else:
        print("No related jobs found.")


# RUN
job_portal()

