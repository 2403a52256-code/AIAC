import sympy as sp

# Define the variable and function
x = sp.symbols('x', real=True)   # ensure x is real
f = 2*x**3 + 4*x + 5

# Compute critical points (set derivative to zero)
df = sp.diff(f, x)
critical_points = sp.solve(df, x)

# Filter only real critical points
critical_points = [cp for cp in critical_points if cp.is_real]

# Second derivative
f2 = sp.diff(f, x, 2)

# Check which critical point yields a minimum
min_points = []
for cp in critical_points:
    sd_val = f2.subs(x, cp)
    if sd_val.is_real and sd_val > 0:
        min_points.append(cp)

print("Critical points:", critical_points)

if min_points:
    print("Function attains minimum at x =", min_points[0])
else:
    print("No minimum for the given function")
