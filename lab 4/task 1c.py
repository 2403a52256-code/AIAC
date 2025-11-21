def is_valid_indian_mobile():
    number = input("Enter an Indian mobile number: ")
    # Remove spaces and hyphens
    number = number.replace(" ", "").replace("-", "")
    if len(number) == 10 and number.isdigit() and number[0] in "6789":
        print("Valid Indian mobile number.")
    else:
        print("Invalid Indian mobile number.")

is_valid_indian_mobile()
