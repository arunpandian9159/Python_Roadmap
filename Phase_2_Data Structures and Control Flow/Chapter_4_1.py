# numbers_demo.py - Working with different number types
import math
import random

# Integer operations
print("=== INTEGER OPERATIONS ===") 
large_number = 123456789012345678901234567890
print(f"Large integer: {large_number}")
print(f"Type: {type(large_number)}")

# Float operations
print("\n=== FLOAT OPERATIONS ===")
pi = 3.14159265359
e = 2.71828
print(f"π = {pi}")
print(f"e = {e}")
print(f"π * e = {pi * e}")
print(f"Rounded: {round(pi * e, 3)}")

# Complex numbers
print("\n=== COMPLEX NUMBERS ===")
z1 = 3 + 4j
z2 = 1 - 2j
print(f"z1 = {z1}")
print(f"z2 = {z2}")
print(f"z1 + z2 = {z1 + z2}")
print(f"z1 * z2 = {z1 * z2}")
print(f"Magnitude of z1: {abs(z1)}")

# Number conversion
print("\n=== NUMBER CONVERSION ===")
string_number = "42"
print(f"String to int: int('{string_number}') = {int(string_number)}")
print(f"Int to float: float({42}) = {float(42)}")
print(f"Float to int: int({3.14}) = {int(3.14)}")

# Mathematical functions
print("\n=== MATHEMATICAL FUNCTIONS ===")
angle = math.pi / 4
print(f"sin({angle}) = {math.sin(angle)}")
print(f"cos({angle}) = {math.cos(angle)}")
print(f"sqrt(16) = {math.sqrt(16)}")
print(f"Random number: {random.randint(1, 100)}")
