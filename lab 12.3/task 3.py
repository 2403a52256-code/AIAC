def profit(A, B):
    return 6 * A + 5 * B

# Constraint limits
points = []


points.append((0, 0))                     # Origin
points.append((0, 5))                     # A=0 -> from A+B=5
points.append((5, 0))                     # B=0 -> from A+B=5
points.append((0, 6))                     # A=0 -> from 3A+2B=12 => B=6
points.append((4, 0))                     # B=0 -> from 3A+2B=12 => A=4


points.append((2, 3))

# Now filter feasible points (those that satisfy all constraints)
feasible = []
for (A, B) in points:
    if A >= 0 and B >= 0 and (A + B <= 5) and (3*A + 2*B <= 12):
        feasible.append((A, B))

# Calculate profits for each feasible point
profits = [(A, B, profit(A, B)) for (A, B) in feasible]

# Find the maximum profit
best = max(profits, key=lambda x: x[2])

# Display results
print("Feasible points and profits:")
for A, B, P in profits:
    print(f"A = {A}, B = {B}, Profit = {P}")

print("\nOptimal solution:")
print(f"Produce {best[0]} units of A and {best[1]} units of B")
print(f"Maximum Profit = Rs {best[2]}")
