import re

def is_valid_indian_mobile(number):
    # Remove spaces and hyphens
    number = number.replace(" ", "").replace("-", "")
    # Indian mobile numbers: 10 digits, start with 6-9
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, number))

mobile = input("Enter an Indian mobile number: ")
if is_valid_indian_mobile(mobile):
    print("Valid Indian mobile number.")
else:
    print("Invalid Indian mobile number.")