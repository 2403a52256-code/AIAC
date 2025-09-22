def grade(score):  # Define a function to map a numeric score to a letter grade
    """
    Convert a numeric score to a letter grade using standard boundaries.
    Args:
        score (int | float): The numeric score to evaluate.
    Returns:
        str: The corresponding letter grade among "A", "B", "C", "D", or "F".
    """
    if score >= 90:  # If the score is 90 or above
        return "A"  # Return grade A
    elif score >= 80:  # Otherwise, if the score is 80-89
        return "B"  # Return grade B
    elif score >= 70:  # Otherwise, if the score is 70-79
        return "C"  # Return grade C
    elif score >= 60:  # Otherwise, if the score is 60-69
        return "D"  # Return grade D
    else:  # Otherwise, for scores below 60
        return "F"  # Return grade F
def main():  # Define an entry point to demonstrate the grading function
    """
    Demonstrate grading for example scores by printing their letter grades.
    """
    examples = [95, 82, 76, 61, 50]  # Create a list of example scores to grade
    for s in examples:  # Loop through each example score
        print(s, grade(s))  # Print the score alongside its computed letter grade
if __name__ == "__main__":  # Execute the demo only when run directly
    main()  # Call the main function
    # Additional test cases for grade function
    print("Test 1 - Expected: A, Got:", grade(100))
    print("Test 2 - Expected: A, Got:", grade(90))
    print("Test 3 - Expected: B, Got:", grade(89))
    print("Test 4 - Expected: B, Got:", grade(80))
    print("Test 5 - Expected: C, Got:", grade(79))
  