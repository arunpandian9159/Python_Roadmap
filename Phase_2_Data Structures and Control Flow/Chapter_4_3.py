#Comprehensive dictionary operations

# Dictionary creation
print("=== DICTIONARY CREATION ===")
student = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8,
    "courses": ["Python", "Data Structures", "Algorithms"]
}

# Alternative creation methods
empty_dict = {}
dict_from_tuples = dict([("a", 1), ("b", 2), ("c", 3)])
dict_comprehension = {x: x**2 for x in range(1, 6)}

print(f"Student: {student}")
print(f"From tuples: {dict_from_tuples}")
print(f"Comprehension: {dict_comprehension}")

# Dictionary operations
print("\n=== DICTIONARY OPERATIONS ===")
print(f"Student name: {student['name']}")
print(f"Student age: {student.get('age', 'Not found')}")
print(f"Student height: {student.get('height', 'Not specified')}")

# Adding and updating
student["graduation_year"] = 2024
student["gpa"] = 3.9  # Update existing key
print(f"Updated student: {student}")

# Dictionary methods
print("\n=== DICTIONARY METHODS ===")
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# Iterating through dictionary
print("\n=== DICTIONARY ITERATION ===")
for key, value in student.items():
    print(f"{key}: {value}")

# Nested dictionaries
print("\n=== NESTED DICTIONARIES ===")
classroom = {
    "student1": {"name": "Alice", "grade": "A"},
    "student2": {"name": "Bob", "grade": "B"},
    "student3": {"name": "Charlie", "grade": "A-"}
}

for student_id, info in classroom.items():
    print(f"{student_id}: {info['name']} - Grade: {info['grade']}")
