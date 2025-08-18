def convert_temperature(value, from_unit, to_unit):
    """
    Convert a temperature between Celsius (C), Fahrenheit (F), and Kelvin (K).

    Args:
        value (float): The temperature value to convert.
        from_unit (str): The current unit ('C', 'F', 'K' or full names).
        to_unit (str): The target unit ('C', 'F', 'K' or full names).

    Returns:
        float: The converted temperature value.

    Raises:
        ValueError: If either unit is invalid.
    """
    def _norm(unit):
        u = str(unit).strip().lower()
        if u in ("c", "celsius"):
            return "c"
        if u in ("f", "fahrenheit"):
            return "f"
        if u in ("k", "kelvin"):
            return "k"
        raise ValueError("Units must be one of: C, F, K (or their full names)")

    f = _norm(from_unit)
    t = _norm(to_unit)

    if f == t:
        return float(value)

    # Convert source to Kelvin as common intermediate
    if f == "c":
        k = float(value) + 273.15
    elif f == "f":
        k = (float(value) - 32.0) * 5.0 / 9.0 + 273.15
    else:  # f == "k"
        k = float(value)

    # Convert Kelvin to target
    if t == "c":
        return k - 273.15
    if t == "f":
        return (k - 273.15) * 9.0 / 5.0 + 32.0
    return k  # t == "k"
