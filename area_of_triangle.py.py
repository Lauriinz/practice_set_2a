def area_of_triangle(side1: float, side2: float, side3: float) -> float:
    '''
    Calculate the area of a triangle using Heron's formula.

    Parameters:
    side1 (float): Length of the first side.
    side2 (float): Length of the second side.
    side3 (float): Length of the third side.

    Returns:
    float: The area of the triangle.
    '''
    # Calculate the semi-perimeter (s)
    s = (side1 + side2 + side3) / 2

    # Calculate the area using Heron's formula
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

    return area

# Example usage:
first_side = 5.0
second_side = 6.0
third_side = 7.0
triangle_area = area_of_triangle(first_side, second_side, third_side)
print(f"The area of the triangle with sides {first_side}, {second_side}, and {third_side} is {triangle_area}")
