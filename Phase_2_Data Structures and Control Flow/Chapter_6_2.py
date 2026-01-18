# for_loop_demo.py - Iterating over sequences
# Basic for loop with range
print("=== BASIC FOR LOOP ===")
for i in range(5):
    print(f"Iteration {i}")

# For loop with custom range
print("\n=== CUSTOM RANGE ===")
for i in range(2, 11, 2):  # Start, stop, step
    print(f"Even number: {i}")

# Iterating over lists
print("\n=== ITERATING OVER LISTS ===")
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits: 
    print(f"I like {fruit}")

# Enumerate for index and value
print("\n=== ENUMERATE ===")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# Iterating over strings
print("\n=== ITERATING OVER STRINGS ===")
word = "Python"
for letter in word:
    print(f"Letter: {letter}")

# Iterating over dictionaries
print("\n=== ITERATING OVER DICTIONARIES ===")
student_grades = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92,
    "Diana": 98
}

for name, grade in student_grades.items():
    print(f"{name}: {grade}%")

# List comprehension (advanced for loop)
print("\n=== LIST COMPREHENSION ===")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested for loops
print("\n=== NESTED FOR LOOPS ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()  # New line after each row
