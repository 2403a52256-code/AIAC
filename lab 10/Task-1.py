def calc_average(marks):
    """
    Calculate the average score from a list of marks.
    Args:
        marks (list of int/float): List containing the marks.
    Returns:
        float: The average score.
    """
    total = 0  # Initialize total to 0
    for m in marks:
        total += m  # Add each mark to total
    average = total / len(marks)  # Calculate average
    return average  # Return the computed average
# List of marks to calculate the average for
marks = [85, 90, 78, 92]
# Print the average score
print("Average Score is", calc_average(marks))
# Test cases for calc_average function
# Test with all positive integers
test_marks1 = [100, 90, 80, 70]
print("Test 1 - Expected: 85.0, Got:", calc_average(test_marks1))
# Test with all the same marks
test_marks2 = [50, 50, 50, 50]
print("Test 2 - Expected: 50.0, Got:", calc_average(test_marks2))
# Test with a single mark
test_marks3 = [75]
print("Test 3 - Expected: 75.0, Got:", calc_average(test_marks3))
# Test with floating point marks
test_marks4 = [88.5, 92.3, 79.7]
print("Test 4 - Expected: {:.2f}, Got: {:.2f}".format((88.5+92.3+79.7)/3, calc_average(test_marks4)))
# Test with zero marks
test_marks5 = [0, 0, 0, 0]
print("Test 5 - Expected: 0.0, Got:", calc_average(test_marks5))
