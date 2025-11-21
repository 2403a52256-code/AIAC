import math

def calculate_factorial():
    try:
        num = int(input("Enter a number to calculate its factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = math.factorial(num)
            print(f"Factorial of {num} is {result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

calculate_factorial()
