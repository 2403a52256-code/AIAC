def parse_students_info(students):
    """
    Parses a list of nested dictionaries representing student information.
    Extracts and prints Full Name, Branch, and SGPA for each student.
    """
    for idx, student in enumerate(students, 1):
        full_name = student.get('Full Name', 'N/A')
        branch = student.get('Branch', 'N/A')
        sgpa = student.get('SGPA', 'N/A')
        print(f"Student {idx}:")
        print(f"  Full Name: {full_name}")
        print(f"  Branch: {branch}")
        print(f"  SGPA: {sgpa}\n")

# Example usage:
if __name__ == "__main__":
    n = int(input("Enter number of students: "))
    students = []
    for _ in range(n):
        full_name = input("Enter Full Name: ")
        branch = input("Enter Branch: ")
        sgpa = float(input("Enter SGPA: "))
        student_info = {
            'Full Name': full_name,
            'Branch': branch,
            'SGPA': sgpa
        }
        students.append(student_info)
    parse_students_info(students)