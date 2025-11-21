def extract_student_details(student_dict):
    
    def flatten(d, parent_key='', sep='_'):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)
    
    flat_dict = flatten(student_dict)
    full_name = flat_dict.get('Full Name') or flat_dict.get('Full_Name')
    branch = flat_dict.get('Branch')
    sgpa = flat_dict.get('SGPA')
    return (full_name, branch, sgpa)
def get_multiple_students():
    students = []
    n = int(input("Enter number of students: "))
    for i in range(n):
        print(f"\nEnter details for student {i+1}:")
        full_name = input("Full Name: ")
        branch = input("Branch: ")
        sgpa = input("SGPA: ")
        try:
            sgpa = float(sgpa)
        except ValueError:
            print("Invalid SGPA. Setting SGPA to 0.0")
            sgpa = 0.0
        # You can nest this dictionary further if needed
        student_dict = {
            'Full Name': full_name,
            'Branch': branch,
            'SGPA': sgpa
        }
        students.append(student_dict)
    return students

def print_student_details(students):
    print("\nStudent Details:")
    for student in students:
        full_name, branch, sgpa = extract_student_details(student)
        print(f"Full Name: {full_name}, Branch: {branch}, SGPA: {sgpa}")

if __name__ == "__main__":
    students = get_multiple_students()
    print_student_details(students)
