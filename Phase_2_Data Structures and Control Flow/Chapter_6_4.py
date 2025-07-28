# nested_for_loop_demo.py - Loops within loops
# Pattern printing
print("=== PATTERN PRINTING ===")

# Right triangle
print("Right triangle:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Number pyramid
print("\nNumber pyramid:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Multiplication table
print("\n=== MULTIPLICATION TABLE ===")
for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        print(f"{product:3d}", end=" ")
    print()

# Matrix operations
print("\n=== MATRIX OPERATIONS ===")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    for element in row:
        print(f"{element:3d}", end=" ")
    print()

# Finding elements in 2D list
print("\nSearching for number 5:")
target = 5
found = False
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            print(f"Found {target} at position ({i}, {j})")
            found = True
            break
    if found:
        break

# Coordinate generation
print("\n=== COORDINATE GENERATION ===")
print("All coordinates in 3x3 grid:")
for x in range(3):
    for y in range(3):
        print(f"({x}, {y})", end=" ")
    print()

# Complex pattern
print("\n=== COMPLEX PATTERN ===")
size = 5
for i in range(size):
    # Leading spaces
    for j in range(size - i - 1):
        print(" ", end="")
    # Stars
    for k in range(2 * i + 1):
        print("*", end="")
    print()
