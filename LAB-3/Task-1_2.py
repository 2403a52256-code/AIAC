def factorial_iterative(n):
    # Error case: factorial is not defined for negative numbers
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")  
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Iterative calculation using a loop
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def get_valid_input():
    while True:
        try:
            user_input = input("Enter a non-negative integer: ").strip()
            
            # Check if user wants to quit
            if user_input.lower() in ['quit', 'exit', 'q']:
                return None
            
            # Convert to integer
            num = int(user_input)
            return num
            
        except ValueError:
            print("Error: Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            return None
def main():
    print("Factorial Calculator using Iteration (Loop)")
    print("=" * 50)
    print("Enter a non-negative integer to calculate its factorial.")
    print("Type 'quit', 'exit', or 'q' to exit the program.")
    print()
    while True:
        # Get user input
        num = get_valid_input()
        # Check if user wants to quit
        if num is None:
            print("Goodbye!")
            break
        # Calculate factorial
        try:
            result = factorial_iterative(num)
            print(f"Factorial of {num} = {result}")
            # Show the calculation breakdown for smaller numbers
            if num <= 10:
                calculation = " × ".join(str(i) for i in range(1, num + 1))
                print(f"Calculation: {calculation} = {result}")
        except ValueError as e:
            print(f"Error: {e}")
        print("-" * 30)
# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_numbers = [0, 1, 5, 10, -1]
    print("Testing Factorial Function:")
    print("=" * 30)
    for num in test_numbers:
        try:
            result = factorial_iterative(num)
            print(f"Factorial of {num} = {result}")
        except ValueError as e:
            print(f"Error for {num}: {e}")
    print("\n" + "=" * 50)
    # Run interactive program
    main()
