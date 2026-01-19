# function_creation_calling.py - Function creation and calling patterns
# Function definition and calling
def calculate_area(length, width):
    """Calculate area of rectangle"""
    area = length * width
    return area

def calculate_circle_area(radius):
    """Calculate area of circle"""
    import math
    return math.pi * radius ** 2 
def get_student_grade(score):
    """Determine grade based on score"""
    if score >= 90: 
        return "A"
    elif score >= 80: 
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
def format_currency(amount, currency="USD"):
    """Format amount as currency"""
    symbols = {"USD": "$", "EUR": "€", "GBP": "£", "JPY": "¥"}
    symbol = symbols.get(currency, "$")
    return f"{symbol}{amount:.2f}"

# Function calling examples
print("=== FUNCTION CALLING EXAMPLES ===")
# Basic function calling
rect_area = calculate_area(10, 5)
print(f"Rectangle area (10x5): {rect_area}")

circle_area = calculate_circle_area(3)
print(f"Circle area (r=3): {circle_area:.2f}")

# Function calling with different arguments
scores = [95, 87, 76, 65, 45]
print("\nStudent grades:")
for i, score in enumerate(scores, 1):
    grade = get_student_grade(score)
    print(f"Student {i}: Score {score} = Grade {grade}")

# Function calling with different parameters
print("\nCurrency formatting:")
amount = 1234.56
currencies = ["USD", "EUR", "GBP", "JPY"]
for curr in currencies:
    formatted = format_currency(amount, curr)
    print(f"{amount} in {curr}: {formatted}")

# Storing functions in variables
print("\n=== FUNCTIONS AS VARIABLES ===")
area_calculator = calculate_area
result = area_calculator(7, 8)
print(f"Using stored function: 7x8 = {result}")

# Functions in data structures
calculators = {
    "rectangle": calculate_area,
    "circle": calculate_circle_area
}

print(f"Rectangle (3x4): {calculators['rectangle'](3, 4)}")
print(f"Circle (r=2): {calculators['circle'](2):.2f}")
