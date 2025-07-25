#Comprehensive string operations

# String creation and basic operations
print("=== STRING BASICS ===")
text = "Python Programming"
print(f"Original: '{text}'")
print(f"Length: {len(text)}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title case: {text.title()}")

# String indexing and slicing
print("\n=== INDEXING AND SLICING ===")
print(f"First character: text[0] = '{text[0]}'")
print(f"Last character: text[-1] = '{text[-1]}'")
print(f"First 6 chars: text[:6] = '{text[:6]}'")
print(f"Last 11 chars: text[7:] = '{text[7:]}'")
print(f"Every 2nd char: text[::2] = '{text[::2]}'")
print(f"Reversed: text[::-1] = '{text[::-1]}'")

# String methods
print("\n=== STRING METHODS ===")
sample = "  Hello, World! Welcome to Python!  "
print(f"Original: '{sample}'")
print(f"Stripped: '{sample.strip()}'")
print(f"Replace: '{sample.replace('World', 'Python')}'")
print(f"Split: {sample.split()}")
print(f"Starts with 'Hello': {sample.strip().startswith('Hello')}")
print(f"Ends with 'Python!': {sample.strip().endswith('Python!')}")

# String formatting
print("\n=== STRING FORMATTING ===")
name = "Alice"
age = 25
score = 95.67

# Old style formatting
old_format = "Name: %s, Age: %d, Score: %.2f" % (name, age, score)
print(f"Old style: {old_format}")

# .format() method
new_format = "Name: {}, Age: {}, Score: {:.2f}".format(name, age, score)
print(f"New style: {new_format}")

# f-strings (recommended)
f_string = f"Name: {name}, Age: {age}, Score: {score:.2f}"
print(f"F-string: {f_string}")

# Advanced f-string formatting
today = "Tuesday"
print(f"Today is {today:>10}")  # Right align
print(f"Score: {score:08.2f}")  # Zero padding
