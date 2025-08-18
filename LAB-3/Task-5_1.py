def convert_temperature():
    """
    Prompt the user for a temperature value and its unit (C/F),
    convert it to the other scale, print, and return the converted value.

    Returns:
        float | None: Converted temperature value if successful, else None.
    """
    try:
        raw_value = input("Enter temperature value: ").strip()
        value = float(raw_value)
        unit = input("Enter unit (C/F): ").strip().lower()

        if unit.startswith("c"):
            converted = (value * 9.0 / 5.0) + 32.0
            print(f"{value:.2f} °C = {converted:.2f} °F")
            return converted
        elif unit.startswith("f"):
            converted = (value - 32.0) * 5.0 / 9.0
            print(f"{value:.2f} °F = {converted:.2f} °C")
            return converted
        else:
            print("Error: Unit must be 'C' or 'F'.")
            return None
    except ValueError:
        print("Error: Please enter a valid numeric temperature.")
        return None


if __name__ == "__main__":
    # One-time run
    convert_temperature()
