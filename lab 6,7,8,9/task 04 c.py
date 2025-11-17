def sum_to_n_for(n):
    total = 0
    for i in range(n):   
        total += (i + 1)
    return total

def sum_to_n_while(n):
    total, i = 0, n
    while i > 0:
        total += i
        i -= 1
    return total

def sum_to_n_recursive(n):
    return 0 if n <= 0 else n + sum_to_n_recursive(n - 1)

def sum_to_n_builtin(n):
    return sum([i for i in range(1, n + 1)])

def sum_to_n_formula(n):
    return n * (n + 1) // 2

print("For loop:", sum_to_n_for(10))
print("While loop:", sum_to_n_while(10))
print("Recursion:", sum_to_n_recursive(10))
print("Built-in sum:", sum_to_n_builtin(10))
print("Formula:", sum_to_n_formula(10))
