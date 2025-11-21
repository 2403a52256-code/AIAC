#Function to reverse a string
def reverse_string(s):
    reversed_s = s[::-1]
    print(reversed_s)

input_str = input("Enter a string: ")
reverse_string(input_str)