#Comprehensive tuple operations

# Tuple creation
print("=== TUPLE CREATION ===")
coordinates = (3, 4)
rgb_color = (255, 128, 0)
mixed_tuple = ("Alice", 25, True, 3.14)
single_element = (42,)  # Note the comma!

print(f"Coordinates: {coordinates}")
print(f"RGB Color: {rgb_color}")
print(f"Mixed tuple: {mixed_tuple}")
print(f"Single element: {single_element}")

# Tuple unpacking
print("\n=== TUPLE UNPACKING ===")
x, y = coordinates
print(f"x = {x}, y = {y}")

name, age, is_student, gpa = mixed_tuple
print(f"Name: {name}, Age: {age}, Student: {is_student}, GPA: {gpa}")

# Tuple methods
print("\n=== TUPLE METHODS ===")
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"Numbers: {numbers}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of first 3: {numbers.index(3)}")
print(f"Length: {len(numbers)}")

# Tuple slicing
print("\n=== TUPLE SLICING ===")
alphabet = tuple("abcdefghijk")
print(f"Full alphabet: {alphabet}")
print(f"First 5: {alphabet[:5]}")
print(f"Last 3: {alphabet[-3:]}")
print(f"Every 2nd: {alphabet[::2]}")

# Named tuples
print("\n=== NAMED TUPLES ===")
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Student = namedtuple('Student', ['name', 'age', 'major'])

p1 = Point(3, 4)
student = Student("Bob", 22, "Physics")

print(f"Point: {p1}")
print(f"Point x: {p1.x}, y: {p1.y}")
print(f"Student: {student}")
print(f"Student name: {student.name}")
