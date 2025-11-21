def is_palindrome():
    s = input("Enter a string: ")
    cleaned = ''.join(c.lower() for c in s if c != ' ')
    if cleaned == cleaned[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")

# Example usage
is_palindrome()