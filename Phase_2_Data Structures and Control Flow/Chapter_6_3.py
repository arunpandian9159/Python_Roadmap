# range_function_demo.py - Mastering the range function

# Single parameter - range(stop)
print("=== range(5) ===")
for i in range(5):
    print(i, end=" ")
print()

# Two parameters - range(start, stop)
print("\n=== range(3, 8) ===")
for i in range(3, 8):
    print(i, end=" ")
print()

# Three parameters - range(start, stop, step)
print("\n=== range(0, 20, 3) ===")
for i in range(0, 20, 3):
    print(i, end=" ")
print()   
# Negative step
print("\n=== range(10, 0, -1) ===")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# Creating lists with range
print("\n=== CREATING LISTS ===")
numbers = list(range(1, 11))
print(f"Numbers 1-10: {numbers}")

even_numbers = list(range(0, 21, 2))
print(f"Even numbers 0-20: {even_numbers}")

# Practical examples
print("\n=== PRACTICAL EXAMPLES ===")

# Multiplication table
number = 7
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")

# Countdown timer
print("\nCountdown:")
for i in range(5, 0, -1):
    print(f"{i}...")
print("Blast off! 🚀")

# Sum of first n natural numbers
n = 10
total = sum(range(1, n + 1))
print(f"\nSum of first {n} natural numbers: {total}")
