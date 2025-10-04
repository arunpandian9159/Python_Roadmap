# functions_demo.py - Basic function concepts
# Simple function
def greet():
    """A simple greeting function"""
    print("Hello, World!")
# Function with parameters
def greet_person(name):
    """Greet a specific person"""
    print(f"Hello, {name}!")

# Function with multiple parameters
def add_numbers(a, b):
    """Add two numbers and return the result"""
    return a + b

# Function with default parameters
def greet_with_title(name, title="Mr./Ms."):
    """Greet with optional title"""
    return f"Hello, {title} {name}!"

# Function with variable arguments (*args)
def sum_all(*numbers):
    """Sum any number of arguments"""
    return sum(numbers)

# Function with keyword arguments (**kwargs)
def print_info(**info):
    """Print information from keyword arguments"""
    for key, value in info.items():
        print(f"{key}: {value}")

# Function examples
print("=== BASIC FUNCTIONS ===")
greet()
greet_person("Alice")

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

print("\n=== DEFAULT PARAMETERS ===")
print(greet_with_title("John"))
print(greet_with_title("Smith", "Dr."))

print("\n=== VARIABLE ARGUMENTS ===")
print(f"Sum of 1,2,3: {sum_all(1, 2, 3)}")
print(f"Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")

print("\n=== KEYWORD ARGUMENTS ===")
print_info(name="Alice", age=25, city="New York")
print_info(product="Laptop", price=999.99, brand="TechCorp")
