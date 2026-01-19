# return_statement_demo.py - Understanding return statements
# Function with single return value
def square(number):
    """Return square of a number"""
    return number ** 2

# Function with multiple return values
def get_name_parts(full_name):
    """Split full name into parts"""
    parts = full_name.split()
    if len(parts) >= 2:
        return parts[0], parts[-1]  # First and last name
    else: 
        return parts[0], ""  # Only first name 
# Function with conditional returns
def divide_numbers(a, b):
    """Divide two numbers with error handling""" 
    if b == 0:
        return None, "Cannot divide by zero"
    else:
        return a / b, "Success"
# Function with early retur
def find_first_even(numbers):
    """Find first even number in list"""
    for num in numbers:
        if num % 2 == 0:
            return num  # Early return when found
    return None  # No even number found

# Function returning different data types
def analyze_text(text):
    """Analyze text and return statistics"""
    words = text.split()
    return {
        "word_count": len(words),
        "character_count": len(text),
        "longest_word": max(words, key=len) if words else "",
        "words": words
    }

# Function with no explicit return (returns None)
def print_banner(message):
    """Print a decorative banner"""
    border = "=" * (len(message) + 4)
    print(border)
    print(f"  {message}")
    print(border)
    # No return statement = returns None

# Examples of return usage
print("=== SINGLE RETURN VALUES ===")
num = 7
squared = square(num)
print(f"Square of {num}: {squared}")

print("\n=== MULTIPLE RETURN VALUES ===")
full_name = "John Doe Smith"
first, last = get_name_parts(full_name)
print(f"Full name: {full_name}")
print(f"First: {first}, Last: {last}")

print("\n=== CONDITIONAL RETURNS ===")
test_cases = [(10, 2), (15, 3), (8, 0)]
for a, b in test_cases:
    result, message = divide_numbers(a, b)
    if result is not None:
        print(f"{a} ÷ {b} = {result:.2f} ({message})")
    else:
        print(f"{a} ÷ {b}: {message}")

print("\n=== EARLY RETURN ===")
number_lists = [[1, 3, 5, 7], [1, 3, 4, 7], [2, 4, 6]]
for numbers in number_lists:
    first_even = find_first_even(numbers)
    if first_even is not None:
        print(f"First even in {numbers}: {first_even}")
    else:
        print(f"No even numbers in {numbers}")

print("\n=== RETURNING COMPLEX DATA ===")
sample_text = "Python programming is fun and powerful"
stats = analyze_text(sample_text)
print(f"Text: '{sample_text}'")
print(f"Statistics: {stats}")

print("\n=== FUNCTIONS WITHOUT RETURN ===")
result = print_banner("Welcome to Python")
print(f"Function returned: {result}")  # Will print None
