# arrays_demo.py - Working with arrays using lists and array module

# Python lists (dynamic arrays)
print("=== PYTHON LISTS (DYNAMIC ARRAYS) ===")

# Creating arrays/lists
numbers = [1, 2, 3, 4, 5]
mixed_array = [1, "hello", 3.14, True]
empty_array = []
print(f"Numbers array: {numbers}")
print(f"Mixed array: {mixed_array}")
print(f"Empty array: {empty_array}")

# Array operations
print("\n=== ARRAY OPERATIONS ===")

# Adding elements
numbers.append(6)  # Add to end
print(f"After append(6): {numbers}")

numbers.insert(0, 0)  # Insert at position
print(f"After insert(0, 0): {numbers}")

numbers.extend([7, 8, 9])  # Add multiple elements
print(f"After extend([7, 8, 9]): {numbers}")
# Removing elements
numbers.remove(0)  # Remove first occurrence
print(f"After remove(0): {numbers}")

popped = numbers.pop()  # Remove and return last
print(f"Popped element: {popped}")
print(f"After pop(): {numbers}")
del numbers[0]  # Delete by index
print(f"After del numbers[0]: {numbers}")

# Array access and slicing
print("\n=== ARRAY ACCESS AND SLICING ===")
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"Original array: {arr}")
print(f"First element: {arr[0]}")
print(f"Last element: {arr[-1]}")
print(f"First three: {arr[:3]}")
print(f"Last three: {arr[-3:]}")
print(f"Every second: {arr[::2]}")

# Array methods
print("\n=== ARRAY METHODS ===")
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"Original: {numbers}")
print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 4: {numbers.index(4)}")

sorted_numbers = sorted(numbers)
print(f"Sorted (new): {sorted_numbers}")

numbers.sort()
print(f"Sorted (in-place): {numbers}")

numbers.reverse()
print(f"Reversed: {numbers}")

# Using array module for typed arrays
print("\n=== ARRAY MODULE (TYPED ARRAYS) ===")
import array

# Create typed arrays
int_array = array.array('i', [1, 2, 3, 4, 5])  # 'i' for integers
float_array = array.array('f', [1.1, 2.2, 3.3])  # 'f' for floats

print(f"Integer array: {int_array}")
print(f"Float array: {float_array}")
print(f"Array type codes: {array.typecodes}")

# Array module operations
int_array.append(6)
print(f"After append: {int_array}")

int_array.extend([7, 8, 9])
print(f"After extend: {int_array}")

# Convert to list and back
as_list = int_array.tolist()
print(f"As list: {as_list}")

new_array = array.array('i', as_list)
print(f"Back to array: {new_array}")

print("\n=== MULTIDIMENSIONAL ARRAYS ===")
# 2D arrays using lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("2D Matrix:")
for row in matrix:
    print(row)

# Accessing 2D array elements
print(f"Element at [1][2]: {matrix[1][2]}")

# Creating 2D array programmatically
rows, cols = 3, 4
array_2d = [[0 for _ in range(cols)] for _ in range(rows)]
print(f"\n3x4 zero matrix: {array_2d}")

# Fill with values
for i in range(rows):
    for j in range(cols):
        array_2d[i][j] = i * cols + j + 1

print("Filled matrix:")
for row in array_2d:
    print(row)

print("\n=== ARRAY COMPREHENSIONS ===")
# Creating arrays with comprehensions
squares = [x**2 for x in range(1, 11)]
print(f"Squares: {squares}")

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# 2D array comprehension
multiplication_table = [[i*j for j in range(1, 6)] for i in range(1, 6)]
print("\nMultiplication table:")
for row in multiplication_table:
    print(row)

print("\n=== PRACTICAL ARRAY EXAMPLES ===")

# Temperature tracking
temperatures = [22.5, 25.1, 23.8, 26.2, 24.9, 21.7, 23.3]
print(f"Temperatures: {temperatures}")
print(f"Average: {sum(temperatures) / len(temperatures):.1f}°C")
print(f"Maximum: {max(temperatures)}°C")
print(f"Minimum: {min(temperatures)}°C")

# Student grades management
students_grades = [
    ["Alice", [85, 92, 78, 96]],
    ["Bob", [76, 88, 82, 79]],
    ["Charlie", [95, 91, 89, 94]]
]

print("\nStudent Grade Summary:")
for name, grades in students_grades:
    average = sum(grades) / len(grades)
    print(f"{name}: Grades {grades}, Average: {average:.1f}")

# Shopping cart
cart = []
products = [
    ("Laptop", 999.99),
    ("Mouse", 29.99),
    ("Keyboard", 79.99)
]

# Add items to cart
for product, price in products:
    cart.append({"product": product, "price": price, "quantity": 1})

print("\nShopping Cart:")
total = 0
for item in cart:
    item_total = item["price"] * item["quantity"]
    total += item_total
    print(f"{item['product']}: ${item['price']:.2f} x {item['quantity']} = ${item_total:.2f}")

print(f"Total: ${total:.2f}")
