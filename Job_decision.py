def job_decision(experience , skills):
    if experience >= 5 and skills >= 4:
        return "eligible"
    elif experience >= 3 and skills >= 3:
        return "interview"
    else:
        return "rejected"
    
applicants = [
      (2 , 1),
      (3 , 2),
      (4 , 3),
      (5 , 4),
      (6 , 5)
]

for applicant in applicants:
    experience = applicant[0]
    skills = applicant[1]
    decision = job_decision(experience , skills)
    print("Experience: " , experience , "Skills: " , skills  , "→" , decision)