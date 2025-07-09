# identifiers_demo.py - Valid and invalid identifiers

# Valid identifiers (variable names)
valid_names = [
    "variable",
    "variable_name",
    "variableName",
    "_private_var",
    "var123",
    "PI",
    "class_name",
    "_",
    "__special__"
]

# Examples of valid identifiers
my_variable = "Valid"
_private = "Valid private variable"
camelCase = "Valid camelCase"
snake_case = "Valid snake_case"
NUMBER_123 = "Valid with numbers"

print("Valid identifiers examples:")
for name in valid_names:
    print(f"✓ {name}")

# Invalid identifiers (would cause SyntaxError)
invalid_examples = [
    "123variable",  # Can't start with number
    "my-variable",  # Hyphen not allowed
    "for",          # Keyword
    "my variable",  # Space not allowed
    "@variable",    # Special characters not allowed
]

print("\nInvalid identifiers (don't use these):")
for name in invalid_examples:
    print(f"✗ {name}")