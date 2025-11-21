def area_of_rectangle(length, breadth):
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    length : float or int
        The length of the rectangle. Must be a positive number.
    breadth : float or int
        The breadth of the rectangle. Must be a positive number.

    Returns
    -------
    float or int
        The area of the rectangle.

    Raises
    ------
    ValueError
        If length or breadth is not a positive number.
    TypeError
        If length or breadth is not a number.
    """
    if not (isinstance(length, (int, float)) and isinstance(breadth, (int, float))):
        raise TypeError("Length and breadth must be numbers.")
    if length <= 0 or breadth <= 0:
        raise ValueError("Length and breadth must be positive numbers.")
    return length * breadth


print(area_of_rectangle(10, 20))