def factorial_febo(n):
    """Return (factorial_of_n, fibonacci_series_up_to_n_terms).

    n must be a non-negative integer. The Fibonacci series starts with 0, 1.
    Example: n=5 -> fib [0, 1, 1, 2, 3]
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    # Factorial of n
    factorial = 1
    for value in range(2, n + 1):
        factorial *= value

    # Fibonacci series up to n terms
    fibonacci_series = []
    if n > 0:
        a, b = 0, 1
        for _ in range(n):
            fibonacci_series.append(a)
            a, b = b, a + b

    return factorial, fibonacci_series


if __name__ == "__main__":
    try:
        user_input = input("Enter a non-negative integer n: ").strip()
        n_val = int(user_input)
        fact, fibo = factorial_febo(n_val)
        print(f"Factorial of {n_val}: {fact}")
        print(f"Fibonacci series ({n_val} terms): {fibo}")
    except (ValueError, TypeError) as exc:
        print(f"Error: {exc}")

