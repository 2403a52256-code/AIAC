def fibonacci(n):
    """
    Recursively calculate the nth Fibonacci number.

    The Fibonacci sequence is defined as:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2) for n > 1

    Parameters:
        n (int): The position in the Fibonacci sequence (must be a non-negative integer).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    # Check for invalid (negative) input
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Base case: F(0) = 0
    if n == 0:
        return 0
    # Base case: F(1) = 1
    elif n == 1:
        return 1
    else:
        # Recursive case: F(n) = F(n-1) + F(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))
print(fibonacci(10))
# --- Explanation Document ---
"""
How the fibonacci(n) function works:

1. The function takes a single argument n, which represents the position in the Fibonacci sequence.
2. It first checks if n is negative. If so, it raises a ValueError, since the Fibonacci sequence is only defined for non-negative integers.
3. If n is 0, the function returns 0 (the first Fibonacci number).
4. If n is 1, the function returns 1 (the second Fibonacci number).
5. For all other values of n (n > 1), the function calls itself recursively to compute fibonacci(n-1) and fibonacci(n-2), and returns their sum.
6. This process continues until the base cases (n == 0 or n == 1) are reached, at which point the recursion unwinds and the final result is returned.

Example usage:
    print(fibonacci(5))  # Output: 5
    print(fibonacci(10)) # Output: 55

Note:
- This implementation is simple and easy to understand, but it is not efficient for large n due to repeated calculations.
- For large values of n, consider using memoization or an iterative approach.
"""
