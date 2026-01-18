#Comprehensive set operations
# Set creation
print("=== SET CREATION ===")
fruits = {"apple", "banana", "orange", "apple"}  # Duplicates removed
print(f"Fruits set: {fruits}")

numbers = set([1, 2, 3, 4, 5, 2, 3])
print(f"Numbers set: {numbers}")

# Set from string 
letters = set("hello")
print(f"Letters from 'hello': {letters}")

# Set operations
print("\n=== SET OPERATIONS ===")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union (A | B): {set_a | set_b}")
print(f"Intersection (A & B): {set_a & set_b}")
print(f"Difference (A - B): {set_a - set_b}")
print(f"Symmetric difference (A ^ B): {set_a ^ set_b}")

# Set methods
print("\n=== SET METHODS ===")
colors = {"red", "green", "blue"}
print(f"Original colors: {colors}")

colors.add("yellow")
print(f"After adding yellow: {colors}")

colors.update(["purple", "orange"])
print(f"After updating with list: {colors}")

colors.remove("green")  # Raises error if not found
print(f"After removing green: {colors}")

colors.discard("pink")  # No error if not found
print(f"After discarding pink (safe): {colors}")

# Set comprehension
print("\n=== SET COMPREHENSION ===")
squares = {x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")
