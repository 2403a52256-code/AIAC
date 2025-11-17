def get_applicant_info():
    name = input("Enter applicant name: ").strip()
    try:
        salary = float(input("Enter applicant salary: ").strip())
    except ValueError:
        print("Invalid salary input. Please enter a numeric value.")
        return None
    try:
        credit_score = int(input("Enter applicant credit score: ").strip())
    except ValueError:
        print("Invalid credit score input. Please enter an integer value.")
        return None
    return {
        "name": name,
        "salary": salary,
        "credit_score": credit_score
    }

def approve_loan(applicant):
    # Loan approval criteria:
    # - Salary must be at least 30,000
    # - Credit score must be at least 650
    # Decision is based solely on salary and credit score.
    if applicant["salary"] >= 30000 and applicant["credit_score"] >= 650:
        return True
    else:
        return False

def main():
    print("=== Loan Approval System ===")
    applicant = get_applicant_info()
    if not applicant:
        return
    if approve_loan(applicant):
        print(f"Loan Approved for {applicant['name']}.")
    else:
        print(f"Loan Denied for {applicant['name']}.")

if __name__ == "__main__":
    main()

# --- Bias Review ---
# The loan approval decision is based solely on salary and credit score.
# The applicant's name (or any other demographic information such as gender) is not used in the decision process.
# Therefore, two applicants with the same salary and credit score will receive the same decision, regardless of their name or gender.

