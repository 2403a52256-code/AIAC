def classify_age_dict(age):
    if age < 0:
        return "Invalid age"
    
    age_groups = {
        "Child": range(0, 13),
        "Teen": range(13, 20),
        "Adult": range(20, 60),
        "Senior": range(60, 200)  # assuming max age as 199
    }
    
    for group, r in age_groups.items():
        if age in r:
            return group
    return "Unknown"

ages_to_test = [5, 15, 35, 65, -3]

for age in ages_to_test:
    print(f"Age: {age} -> Group: {classify_age_dict(age)}")

