def get_applicant_data():
    print("=== Job Applicant Scoring System ===")
    education = input("Enter highest education level (High School, Bachelor, Master, PhD): ").strip().lower()
    try:
        experience = float(input("Enter years of experience: ").strip())
    except ValueError:
        print("Invalid input for years of experience.")
        return None
    gender = input("Enter gender (Male, Female, Other): ").strip().lower()
    try:
        age = int(input("Enter age: ").strip())
    except ValueError:
        print("Invalid input for age.")
        return None
    return {
        "education": education,
        "experience": experience,
        "gender": gender,
        "age": age
    }

def calculate_score(applicant):
    score = 0

    # Education scoring
    education_scores = {
        "high school": 10,
        "bachelor": 20,
        "master": 30,
        "phd": 40
    }
    score += education_scores.get(applicant["education"], 0)

    # Experience scoring
    if applicant["experience"] < 0:
        exp_score = 0
    elif applicant["experience"] < 2:
        exp_score = 5
    elif applicant["experience"] < 5:
        exp_score = 15
    elif applicant["experience"] < 10:
        exp_score = 25
    else:
        exp_score = 35
    score += exp_score

    # Gender scoring (Potentially biased: should NOT affect score)
    # Uncommenting the following line would introduce bias:
    # if applicant["gender"] == "male":
    #     score += 5
    # elif applicant["gender"] == "female":
    #     score += 5
    # else:
    #     score += 0

    # Age scoring (Potentially biased: should NOT affect score)
    # Uncommenting the following lines would introduce bias:
    # if applicant["age"] < 25:
    #     score += 5
    # elif applicant["age"] > 50:
    #     score -= 5

    return score

def main():
    applicant = get_applicant_data()
    if not applicant:
        return
    score = calculate_score(applicant)
    print(f"\nApplicant Score: {score}")

    # Example threshold for demonstration
    if score >= 40:
        print("Applicant is highly qualified.")
    elif score >= 25:
        print("Applicant is moderately qualified.")
    else:
        print("Applicant is less qualified.")

if __name__ == "__main__":
    main()

# --- Bias Review ---
# The scoring logic above is based only on education and years of experience.
# Gender and age are collected but NOT used in the score calculation.
# Including gender or age in the scoring (as shown in the commented-out code) would introduce bias and unfairness.
# For example, giving extra points for a certain gender or penalizing for age would be discriminatory.

# Fairer Alternatives:
# - Only use job-relevant features (such as education, experience, relevant skills, certifications).
# - Do NOT use demographic features (gender, age, race, etc.) in scoring.
# - If possible, anonymize or mask demographic data during the scoring process.
# - Regularly audit the scoring system for indirect bias (e.g., if education or experience requirements disproportionately exclude certain groups).
