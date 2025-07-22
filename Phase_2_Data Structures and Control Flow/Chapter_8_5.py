# lambda_functions_demo.py - Anonymous functions
# Basic lambda functions
print("=== BASIC LAMBDA FUNCTIONS ===")

# Simple lambda
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple arguments
add = lambda x, y: x + y
print(f"Add 3 + 7: {add(3, 7)}")

# Lambda with conditional
max_of_two = lambda a, b: a if a > b else b
print(f"Max of 10, 15: {max_of_two(10, 15)}")

print("\n=== LAMBDA WITH MAP() ===")
numbers = [1, 2, 3, 4, 5]
print(f"Original numbers: {numbers}")

# Square all numbers
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared: {squared}")

# Convert to strings
strings = list(map(lambda x: f"Number: {x}", numbers))
print(f"As strings: {strings}")

# Temperature conversion
fahrenheit = [32, 68, 86, 104]
celsius = list(map(lambda f: (f - 32) * 5/9, fahrenheit))
print(f"Fahrenheit: {fahrenheit}")
print(f"Celsius: {[round(c, 1) for c in celsius]}")

print("\n=== LAMBDA WITH FILTER() ===")
numbers = list(range(1, 21))
print(f"Numbers 1-20: {numbers}")

# Filter even numbers
even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even}")

# Filter numbers greater than 10
greater_than_10 = list(filter(lambda x: x > 10, numbers))
print(f"Greater than 10: {greater_than_10}")

# Filter words by length
words = ["python", "is", "awesome", "programming", "fun"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(f"Words longer than 5 chars: {long_words}")

print("\n=== LAMBDA WITH SORTED() ===")
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("Diana", 96)
]

# Sort by grade (second element)
by_grade = sorted(students, key=lambda student: student[1])
print(f"Sorted by grade: {by_grade}")

# Sort by name length
by_name_length = sorted(students, key=lambda student: len(student[0]))
print(f"Sorted by name length: {by_name_length}")

# Sort by grade (descending)
by_grade_desc = sorted(students, key=lambda student: student[1], reverse=True)
print(f"Sorted by grade (desc): {by_grade_desc}")

print("\n=== LAMBDA WITH REDUCE() ===")
from functools import reduce

numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(f"Sum: {total}")

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum: {maximum}")

# Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")

print("\n=== ADVANCED LAMBDA EXAMPLES ===")

# Lambda in list comprehension
squares_comp = [(lambda x: x**2)(x) for x in range(1, 6)]
print(f"Squares comprehension: {squares_comp}")

# Lambda for data processing
sales_data = [
    {"product": "Laptop", "price": 1200, "quantity": 2},
    {"product": "Mouse", "price": 25, "quantity": 5},
    {"product": "Keyboard", "price": 75, "quantity": 3}
]

# Calculate total for each item
totals = list(map(lambda item: {
    "product": item["product"],
    "total": item["price"] * item["quantity"]
}, sales_data))

print("Sales totals:")
for item in totals:
    print(f"  {item['product']}: ${item['total']}")

# Find expensive items
expensive = list(filter(lambda item: item["price"] > 50, sales_data))
print(f"Expensive items: {[item['product'] for item in expensive]}")

print("\n=== LAMBDA VS REGULAR FUNCTIONS ===")

# Regular function
def regular_multiply(x, y):
    return x * y

# Lambda function
lambda_multiply = lambda x, y: x * y

# Both do the same thing
print(f"Regular function: {regular_multiply(4, 5)}")
print(f"Lambda function: {lambda_multiply(4, 5)}")

# Lambda for immediate use (common pattern)
result = (lambda x: x ** 3)(4)  # Cube of 4
print(f"Immediate lambda use: {result}")

# Lambda in dictionary
operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y if y != 0 else "Cannot divide by zero"
}

print("\nUsing lambda in dictionary:")
for op, func in operations.items():
    result = func(10, 3)
    print(f"{op}: {result}")
