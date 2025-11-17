def generate_multiples(num, count):
    return [num * i for i in range(1, count + 1)]

def print_multiples_for(num):
    print(f"First 10 multiples of {num} using for loop:")
    multiples = generate_multiples(num, 10)
    for value in multiples:
        print(value, end=" ")
    print()

def print_multiples_while(num):
    print(f"First 10 multiples of {num} using while loop:")
    multiples = generate_multiples(num, 10)
    i = 0
    while i < len(multiples):
        print(multiples[i], end=" ")
        i += 1
    print()

number = 10
print_multiples_for(number)
print_multiples_while(number)