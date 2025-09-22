def get_students():  # Define a function to provide the list of student names
    """
    Return a predefined list of student names.
    Returns:
        list[str]: A list containing student names.
    """
    students = ["Alice", "Bob", "Charlie"]  # Create a list of student names
    return students  # Return the list of students
def greet_student(name):  # Define a function to greet a single student
    """
    Print and return a welcome message for a single student.
    Args:
        name (str): The student's name to greet.
    Returns:
        str: The greeting message that was printed.
    """
    message = "Welcome {}".format(name)  # Build a formatted greeting message
    print(message)  # Output the greeting message to the console
    return message  # Return the message (useful for testing)
def greet_all_students(students):  # Define a function to greet all students in a list
    """
    Greet each student in the provided list.
    Args:
        students (list[str]): The list of student names to greet.
    """
    for name in students:  # Iterate over every name in the students list
        greet_student(name)  # Greet the current student by name
def main():  # Define the program's main entry point
    """
    Load the student list and greet each student.
    """
    students = get_students()  # Obtain the list of students
    greet_all_students(students)  # Greet every student in the list
if __name__ == "__main__":  # Ensure main() runs only when executed directly
    main()  # Call the main function to run the greetings demo
    # Test cases for get_students
    print("Test get_students - Expected: ['Alice', 'Bob', 'Charlie'], Got:", get_students())
    # Test cases for greet_student
    print("Test greet_student('Alice') - Expected: Welcome Alice, Got:", greet_student('Alice'))
    print("Test greet_student('Bob') - Expected: Welcome Bob, Got:", greet_student('Bob'))
    # Test cases for greet_all_students
    print("Test greet_all_students(['Dave', 'Eve']):")
    greet_all_students(['Dave', 'Eve'])  # Should print Welcome Dave and Welcome Eve
    # Test greet_all_students with empty list
    print("Test greet_all_students([]):")
    greet_all_students([])  # Should not print anything
