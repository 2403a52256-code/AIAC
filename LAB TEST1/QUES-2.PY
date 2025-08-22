class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = list(marks)
    def calculate_grade(self):
        if not self.marks:
            return "N/A"
        average = sum(self.marks) / len(self.marks)
        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        return "F"
    def display_details(self):
        print(f"Name      : {self.name}")
        print(f"Roll No   : {self.roll_no}")
        print(f"Marks     : {self.marks}")
        print(f"Grade     : {self.calculate_grade()}")
if __name__ == "__main__":
    try:
        name = input("Enter student name: ").strip()
        roll_no = input("Enter roll number: ").strip()
        count = int(input("How many subjects? ").strip())
        marks = []
        for i in range(1, count + 1):
            mark = float(input(f"Enter mark {i}: ").strip())
            marks.append(mark)

        student = Student(name=name, roll_no=roll_no, marks=marks)
        print("\n--- Student Details ---")
        student.display_details()
    except ValueError as exc:
        print(f"Error: {exc}")

