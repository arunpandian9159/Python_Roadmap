#all types of operators

# Arithmetic operators
a, b = 10, 3
print("=== ARITHMETIC OPERATORS ===")
print(f"{a} + {b} = {a + b}")    # Addition
print(f"{a} - {b} = {a - b}")    # Subtraction
print(f"{a} * {b} = {a * b}")    # Multiplication
print(f"{a} / {b} = {a / b}")    # Division
print(f"{a} // {b} = {a // b}")  # Floor division
print(f"{a} % {b} = {a % b}")    # Modulus
print(f"{a} ** {b} = {a ** b}")  # Exponentiation

# Comparison operators
print("\n=== COMPARISON OPERATORS ===")
x, y = 5, 8
print(f"{x} == {y}: {x == y}")   # Equal
print(f"{x} != {y}: {x != y}")   # Not equal
print(f"{x} < {y}: {x < y}")     # Less than
print(f"{x} > {y}: {x > y}")     # Greater than
print(f"{x} <= {y}: {x <= y}")   # Less than or equal
print(f"{x} >= {y}: {x >= y}")   # Greater than or equal

# Logical operators
print("\n=== LOGICAL OPERATORS ===")
p, q = True, False
print(f"{p} and {q}: {p and q}")
print(f"{p} or {q}: {p or q}")
print(f"not {p}: {not p}")

# Assignment operators
print("\n=== ASSIGNMENT OPERATORS ===")
num = 10
print(f"Initial value: {num}")
num += 5  # num = num + 5
print(f"After +=5: {num}")
num *= 2  # num = num * 2
print(f"After *=2: {num}")
num //= 3  # num = num // 3
print(f"After //=3: {num}")