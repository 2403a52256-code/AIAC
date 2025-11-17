def sum_even_odd(numbers):
    """
    Returns the sum of even and odd numbers in the given list.

    Args:
        numbers (list of int): List of integers.

    Returns:
        tuple: (sum_even, sum_odd) where sum_even is the sum of even numbers,
               and sum_odd is the sum of odd numbers.
    """
    sum_even = sum(n for n in numbers if n % 2 == 0)
    sum_odd = sum(n for n in numbers if n % 2 != 0)
    return sum_even, sum_odd
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    even_sum, odd_sum = sum_even_odd(nums)
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")