def factorial(n):
    # Error case: factorial is not defined for negative numbers
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Calculate factorial using a loop
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# Test the function
if __name__ == "__main__":
    # Test cases
    test_numbers = [0, 1, 5, 10]
    print("Testing factorial function:")
    print("=" * 30)
    for num in test_numbers:
        try:
            result = factorial(num)
            print(f"factorial({num}) = {result}")
        except ValueError as e:
            print(f"Error for {num}: {e}")
    # Test with negative number
    try:
        result = factorial(-1)
        print(f"factorial(-1) = {result}")
    except ValueError as e:
        print(f"Error for -1: {e}")
    # Interactive testing - run only once
    print("\n" + "=" * 30)
    print("Interactive Testing")
    print("Enter a non-negative integer:")
    
    try:
        user_input = input("Enter a number: ").strip()
        num = int(user_input)
        result = factorial(num)
        print(f"factorial({num}) = {result}")
    except ValueError as e:
        print(f"Error: {e}")
