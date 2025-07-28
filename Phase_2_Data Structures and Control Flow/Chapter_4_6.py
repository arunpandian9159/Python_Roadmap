# boolean_demo.py - Boolean operations and truth values
# Boolean basics
print("=== BOOLEAN BASICS ===")
is_sunny = True
is_raining = False

print(f"Is sunny: {is_sunny}")
print(f"Is raining: {is_raining}")
print(f"Type of True: {type(is_sunny)}")

# Boolean operations
print("\n=== BOOLEAN OPERATIONS ===")
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")
print(f"not False: {not False}")

# Boolean conversion
print("\n=== BOOLEAN CONVERSION ===")
print(f"bool(1): {bool(1)}")
print(f"bool(0): {bool(0)}")
print(f"bool('hello'): {bool('hello')}")
print(f"bool(''): {bool('')}")
print(f"bool([1, 2, 3]): {bool([1, 2, 3])}")
print(f"bool([]): {bool([])}")
print(f"bool(None): {bool(None)}")

# Truth values in conditionals
print("\n=== TRUTH VALUES IN CONDITIONALS ===")
values = [0, 1, "", "hello", [], [1, 2], None, {}, {"a": 1}]

for value in values:
    if value:
        print(f"{repr(value)} is truthy")
    else:
        print(f"{repr(value)} is falsy")

# Boolean in calculations
print("\n=== BOOLEAN IN CALCULATIONS ===")
print(f"True + True = {True + True}")  # True = 1, False = 0
print(f"True * 5 = {True * 5}")
print(f"False * 100 = {False * 100}")

# Short-circuit evaluation
print("\n=== SHORT-CIRCUIT EVALUATION ===")
def check_value(x):
    print(f"Checking {x}")
    return x > 5

# Only the first function is called (False and ...)
result1 = False and check_value(10)
print(f"Result 1: {result1}")

# Only the first function is called (True or ...)
result2 = True or check_value(10)
print(f"Result 2: {result2}")
