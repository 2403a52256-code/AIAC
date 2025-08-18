RATE_PER_UNIT = 6.50  # Fixed rate per unit (change as needed)


def calculate_electricity_bill(units_consumed, rate_per_unit=RATE_PER_UNIT):
	"""
	Calculate electricity bill using a fixed rate per unit.

	Args:
		units_consumed (float): Number of units consumed (must be non-negative)
		rate_per_unit (float): Fixed rate per unit

	Returns:
		float: Total bill amount
	"""
	if units_consumed < 0:
		raise ValueError("Units consumed cannot be negative")
	if rate_per_unit < 0:
		raise ValueError("Rate per unit cannot be negative")
	return units_consumed * rate_per_unit


if __name__ == "__main__":
	print("Electricity Bill Calculator (Fixed Rate)")
	print("=" * 40)
	try:
		units = float(input("Enter units consumed: ").strip())
		amount = calculate_electricity_bill(units)
		print(f"Rate per unit: ₹{RATE_PER_UNIT:.2f}")
		print(f"Total amount:  ₹{amount:.2f}")
	except ValueError as e:
		print(f"Error: {e}")
