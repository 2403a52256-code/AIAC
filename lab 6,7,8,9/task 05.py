def greet_user():
    name = input("Enter your name: ").strip()
    gender = input("Enter your gender (male/female/other): ").strip().lower()

    if gender == "male":
        title = "Mr."
    elif gender == "female":
        title = "Ms."
    elif gender == "other":
        title = ""   # No gendered title for 'other'
    else:
        title = ""   # Default if input is unexpected

    # Use .strip() to clean up extra spaces if no title
    print(f"Hello, {title} {name}! Welcome".strip())

# Example run
greet_user()
