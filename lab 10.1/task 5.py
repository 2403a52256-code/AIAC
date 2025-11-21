import time

# Find squares of numbers using list comprehension and measure execution time
start_time = time.time()
nums = list(range(1, 1000000))
squares = [n**2 for n in nums]
end_time = time.time()

print(len(squares))
print(f"Execution time: {end_time - start_time:.4f} seconds")
