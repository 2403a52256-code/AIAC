def calculate_power_bill(units_consumed, customer_type="residential"):
    # Rate structure (per unit in currency)
    rates = {
        "residential": {
            "slab1": {"limit": 100, "rate": 5.0},
            "slab2": {"limit": 200, "rate": 7.0},
            "slab3": {"limit": float('inf'), "rate": 10.0}},
        "commercial": {
            "slab1": {"limit": 200, "rate": 8.0},
            "slab2": {"limit": 500, "rate": 12.0},
            "slab3": {"limit": float('inf'), "rate": 15.0}},
        "industrial": {
            "slab1": {"limit": 500, "rate": 10.0},
            "slab2": {"limit": 1000, "rate": 15.0},
            "slab3": {"limit": float('inf'), "rate": 20.0}}}
    # Fixed charges
    fixed_charges = {
        "residential": 50,
        "commercial": 100,
        "industrial": 200
    }
    # Get rates for customer type
    customer_rates = rates[customer_type]
    fixed_charge = fixed_charges[customer_type]
    # Calculate bill breakdown
    remaining_units = units_consumed
    total_amount = 0
    breakdown = []
    # Calculate for each slab
    for slab_name, slab_data in customer_rates.items():
        if remaining_units <= 0:
            break
        if slab_name == "slab1":
            units_in_slab = min(remaining_units, slab_data["limit"])
        elif slab_name == "slab2":
            units_in_slab = min(remaining_units, slab_data["limit"] - customer_rates["slab1"]["limit"])
        else:  # slab3
            units_in_slab = remaining_units            
        if units_in_slab > 0:
            slab_amount = units_in_slab * slab_data["rate"]
            total_amount += slab_amount
            breakdown.append({
                "slab": slab_name,
                "units": units_in_slab,
                "rate": slab_data["rate"],
                "amount": slab_amount
            })
            remaining_units -= units_in_slab
    # Add fixed charge
    total_amount += fixed_charge
    # Calculate tax (5% of energy charges)
    energy_charges = total_amount - fixed_charge
    tax = energy_charges * 0.05
    total_amount += tax
    return {
        "customer_type": customer_type,
        "units_consumed": units_consumed,
        "breakdown": breakdown,
        "energy_charges": energy_charges,
        "fixed_charge": fixed_charge,
        "tax": tax,
        "total_amount": total_amount
    }
def get_user_input():
    """
    Get user input for power bill calculation with validation.
    
    Returns:
        tuple: (units_consumed, customer_type)
    """
    print("Power Bill Calculator")
    print("=" * 30)
    # Get units consumed
    while True:
        try:
            units = float(input("Enter units consumed: "))
            if units < 0:
                print("Error: Units consumed cannot be negative.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number.")
    # Get customer type
    print("\nCustomer Types:")
    print("1. Residential")
    print("2. Commercial") 
    print("3. Industrial")
    while True:
        try:
            choice = int(input("Select customer type (1-3): "))
            if choice == 1:
                customer_type = "residential"
                break
            elif choice == 2:
                customer_type = "commercial"
                break
            elif choice == 3:
                customer_type = "industrial"
                break
            else:
                print("Error: Please select 1, 2, or 3.")
        except ValueError:
            print("Error: Please enter a valid number.")
    return units, customer_type
def display_bill(bill_details):
    """
    Display the power bill in a formatted way.
    
    Args:
        bill_details (dict): Bill calculation details
    """
    print("\n" + "=" * 50)
    print("POWER BILL STATEMENT")
    print("=" * 50)
    print(f"Customer Type: {bill_details['customer_type'].title()}")
    print(f"Units Consumed: {bill_details['units_consumed']:.2f}")
    print("-" * 50)

    print("ENERGY CHARGES BREAKDOWN:")
    for item in bill_details['breakdown']:
        print(f"  {item['slab'].upper()}: {item['units']:.2f} units × ₹{item['rate']:.2f} = ₹{item['amount']:.2f}")
    print("-" * 50)
    print(f"Energy Charges:     ₹{bill_details['energy_charges']:.2f}")
    print(f"Fixed Charge:       ₹{bill_details['fixed_charge']:.2f}")
    print(f"Tax (5%):           ₹{bill_details['tax']:.2f}")
    print("=" * 50)
    print(f"TOTAL AMOUNT:       ₹{bill_details['total_amount']:.2f}")
    print("=" * 50)
# Test the function
if __name__ == "__main__":
    # Test cases
    test_cases = [
        (50, "residential"),
        (150, "residential"),
        (300, "commercial"),
        (800, "industrial"),
        (1200, "industrial")]
    print("Testing Power Bill Calculator:")
    print("=" * 40)
    for units, customer_type in test_cases:
        bill = calculate_power_bill(units, customer_type)
        print(f"\nTest Case: {units} units, {customer_type} customer")
        display_bill(bill)
    
    # Interactive testing
    print("\n" + "=" * 50)
    print("Interactive Power Bill Calculator")
    print("=" * 50)
    
    try:
        units, customer_type = get_user_input()
        bill_details = calculate_power_bill(units, customer_type)
        display_bill(bill_details)
        
    except Exception as e:
        print(f"Error: {e}")
