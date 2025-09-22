def percentage_of(base, percent):  # Define a function to compute 'percent' percent of 'base'
 """
 Compute the percentage value of a base number.

 Args:
     base (float | int): The base value from which to take a percentage.
     percent (float | int): The percentage to apply to the base.

 Returns:
     float: The value equal to (base × percent) / 100.
 """
 result = base * percent / 100  # Multiply base by percent and divide by 100 to get the percentage
 return result  # Return the computed percentage value
def main():  # Define the main function to demonstrate usage
 """
 Demonstrate percentage calculation with example values and print the result.
 """
 a = 200  # Example base value
 b = 15  # Example percent value
 print(percentage_of(a, b))  # Compute 15% of 200 and print the result
if __name__ == "__main__":  # Execute the demo only when run as a script
 main()  # Call the main function
 print("Test 1 - Expected: 30.0, Got:", percentage_of(200, 15))
 print("Test 2 - Expected: 0.0, Got:", percentage_of(0, 50))
 print("Test 3 - Expected: 100.0, Got:", percentage_of(1000, 10))
 print("Test 4 - Expected: 7.5, Got:", percentage_of(75, 10))
 print("Test 5 - Expected: -20.0, Got:", percentage_of(-200, 10))
