def swap(a, b):
    if a > b:
        return b, a
    else:
        return a, b
def sort_three_numbers(a, b, c):
    """
    Sort three numbers in ascending order using helper functions.
    
    Args:
        a: First number
        b: Second number
        c: Third number
        
    Returns:
        tuple: Three numbers sorted in ascending order (smallest, middle, largest)
    """
    # Sort first two numbers
    smallest, temp = swap(a, b)
    # Sort the result with the third number
    smallest, middle = swap(smallest, c)
    # Sort the remaining two numbers
    middle, largest = swap(middle, temp)
    return smallest, middle, largest
def get_user_input():
    """
    Get three numbers from user input with error handling.
    
    Returns:
        tuple: Three valid numbers entered by user
    """
    numbers = []
    for i in range(3):
        while True:
            try:
                num = float(input(f"Enter number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Error: Please enter a valid number.")
    return numbers[0], numbers[1], numbers[2]
# Test the function
if __name__ == "__main__":
    # Test cases
    test_cases = [
        (3, 1, 2),
        (5, 5, 5),
        (10, 5, 1),
        (1, 2, 3),
        (3, 2, 1),
        (-5, 10, -3) ]
    print("Testing sort_three_numbers function:")
    print("=" * 40)
    for a, b, c in test_cases:
        sorted_nums = sort_three_numbers(a, b, c)
        print(f"Input: ({a}, {b}, {c}) -> Sorted: {sorted_nums}")
    print("\n" + "=" * 40)
    print("Interactive Testing")
    print("Enter three numbers to sort:")
    try:
        num1, num2, num3 = get_user_input()
        sorted_result = sort_three_numbers(num1, num2, num3)
        print(f"Original numbers: ({num1}, {num2}, {num3})")
        print(f"Sorted numbers: {sorted_result}")
        # Show the sorting process
        print("\nSorting process:")
        print(f"Step 1: Compare {num1} and {num2}")
        temp1, temp2 = swap(num1, num2)
        print(f"        Result: {temp1}, {temp2}")
        print(f"Step 2: Compare {temp1} and {num3}")
        smallest, temp3 = swap(temp1, num3)
        print(f"        Result: {smallest}, {temp3}")
        print(f"Step 3: Compare {temp3} and {temp2}")
        middle, largest = swap(temp3, temp2)
        print(f"        Final: {smallest}, {middle}, {largest}")
    except Exception as e:
        print(f"Error: {e}")
