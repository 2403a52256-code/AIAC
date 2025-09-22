def area_of_rectangle(length, breadth):  # Define a function that computes area of a rectangle
    """
    Compute the area of a rectangle using the formula: area = length × breadth.

    Args:
        length (float | int): The length of the rectangle.
        breadth (float | int): The breadth (width) of the rectangle.

    Returns:
        float: The computed area of the rectangle.
    """
    area = length * breadth  # Multiply length by breadth to get the area
    return area  # Return the computed area


def main():  # Define the main entry point for demonstration
    """
    Demonstrate rectangle area calculation with an example input and output.
    """
    example_length = 10  # Example length value
    example_breadth = 20  # Example breadth value
    print(area_of_rectangle(example_length, example_breadth))  # Print the calculated area


if __name__ == "__main__":  # Run the demo only when executed directly
    main()  # Invoke the main function
    # Test cases for area_of_rectangle function
    print("Test 1 - Expected: 200, Got:", area_of_rectangle(10, 20))
    print("Test 2 - Expected: 0, Got:", area_of_rectangle(0, 15))
    print("Test 3 - Expected: 56.25, Got:", area_of_rectangle(7.5, 7.5))
    print("Test 4 - Expected: -30, Got:", area_of_rectangle(-5, 6))
    print("Test 5 - Expected: 0, Got:", area_of_rectangle(0, 0))
    print("Test 6 - Expected: 24, Got:", area_of_rectangle(3, 8))
