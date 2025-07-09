#Different types of comments

# This is a single-line comment
x = 5  # This is an inline comment

"""
This is a multi-line comment
(also called a docstring when used for documentation)
It can span multiple lines
"""


def calculate_area(radius):
    """
    Calculate thea of a circe arle

    Args:
        radius (float): The radius of the circle

    Returns:
        float: The area of the circle
    """
    return 3.14159 * radius ** 2


# Good commenting practice
area = calculate_area(5)  # Calculate area for radius = 5
print(f"Area: {area}")

print("====================================================================================================================")

