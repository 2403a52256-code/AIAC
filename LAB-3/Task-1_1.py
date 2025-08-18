def factorial(n):
    if n == 0:
        return 1
    # Error case: factorial is not defined for negative numbers
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)
# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_numbers = [0, 1, 5, 10]  
    print("Factorial Calculator using Recursion")
    print("=" * 40)
    for num in test_numbers:
        try:
            result = factorial(num)
            print(f"Factorial of {num} = {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except RecursionError:
            print(f"Error: Number {num} is too large for recursion limit")
    # Interactive testing
    print("\n" + "=" * 40)
    print("Interactive Testing")
    print("Enter a non-negative integer (or 'quit' to exit):")
    
    while True:
        user_input = input("Enter a number: ").strip()
        if user_input.lower() == 'quit':
            break  
        try:
            num = int(user_input)
            result = factorial(num)
            print(f"Factorial of {num} = {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except RecursionError:
            print("Error: Number too large for recursion limit")
