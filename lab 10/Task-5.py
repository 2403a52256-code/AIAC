def generate_numbers(start, stop):  # Define a function to build a list of integers using a loop
    """
    Generate a list of consecutive integers from start (inclusive) to stop (exclusive).
    Args:
        start (int): The first integer to include.
        stop (int): One past the last integer to include.
    Returns:
        list[int]: List of integers [start, start+1, ..., stop-1].
    """
    numbers = []  # Initialize an empty list to collect integers
    for value in range(start, stop):  # Loop over each integer in the specified range
        numbers.append(value)  # Append the current integer to the list
    return numbers  # Return the populated list of integers
def compute_squares(values):  # Define a function to compute squares using a loop
    """
    Compute squares for each integer in the provided iterable of values.
    Args:
        values (iterable[int]): Sequence of integers to square.
    Returns:
        list[int]: Squares corresponding to the input values.
    """
    squares = []  # Initialize an empty list to collect squares
    for number in values:  # Iterate through each value in the input sequence
        square = number ** 2  # Compute the square of the current number
        squares.append(square)  # Append the computed square to the list
    return squares  # Return the list of computed squares
def main():  # Define the main entry point to orchestrate the workflow
    """
    Build a list of numbers using loops, square them with loops, and print the count.
    """
    nums = generate_numbers(1, 1000000)  # Generate integers from 1 up to (but not including) 1,000,000
    squares = compute_squares(nums)  # Compute squares for each generated integer
    print(len(squares))  # Print the total number of computed squares
if __name__ == "__main__":  # Execute main only when the script is run directly
    main()  # Call the main function
    # Test cases for generate_numbers
    print("Test generate_numbers(0, 5) - Expected: [0, 1, 2, 3, 4], Got:", generate_numbers(0, 5))
    print("Test generate_numbers(3, 3) - Expected: [], Got:", generate_numbers(3, 3))
    print("Test generate_numbers(-2, 2) - Expected: [-2, -1, 0, 1], Got:", generate_numbers(-2, 2))
    print("Test generate_numbers(5, 7) - Expected: [5, 6], Got:", generate_numbers(5, 7))
    # Test cases for compute_squares
    print("Test compute_squares([1, 2, 3]) - Expected: [1, 4, 9], Got:", compute_squares([1, 2, 3]))
    print("Test compute_squares([]) - Expected: [], Got:", compute_squares([]))
    print("Test compute_squares([-2, 0, 2]) - Expected: [4, 0, 4], Got:", compute_squares([-2, 0, 2]))
    print("Test compute_squares([10]) - Expected: [100], Got:", compute_squares([10]))
