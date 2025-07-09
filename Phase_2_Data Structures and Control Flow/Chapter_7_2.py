# string_formatting.py - Modern string formatting techniques

# Variables for examples
name = "Alice"
age = 25
salary = 55000.75
percentage = 0.847

print("=== OLD STYLE FORMATTING (%) ===")
old_style = "Name: %s, Age: %d, Salary: $%.2f" % (name, age, salary)
print(old_style)

print("\n=== .format() METHOD ===")
# Basic usage
format_basic = "Name: {}, Age: {}, Salary: ${:.2f}".format(name, age, salary)
print(format_basic)

# With positional arguments
format_positional = "Name: {0}, Age: {1}, In 10 years: {1} + 10 = {2}".format(name, age, age + 10)
print(format_positional)

# With keyword arguments
format_keyword = "Name: {n}, Age: {a}, Salary: ${s:.2f}".format(n=name, a=age, s=salary)
print(format_keyword)

print("\n=== F-STRINGS (RECOMMENDED) ===")
# Basic f-string
f_basic = f"Name: {name}, Age: {age}, Salary: ${salary:.2f}"
print(f_basic)

# With expressions
f_expression = f"Name: {name.upper()}, Next year age: {age + 1}"
print(f_expression)

# With formatting
f_formatted = f"Percentage: {percentage:.2%}, Salary: ${salary:,.2f}"
print(f_formatted)

print("\n=== ADVANCED F-STRING FORMATTING ===")
# Alignment and padding
print(f"Left aligned: '{name:<15}'")
print(f"Right aligned: '{name:>15}'")
print(f"Center aligned: '{name:^15}'")
print(f"Zero padded number: '{age:05d}'")

# Date formatting
from datetime import datetime
now = datetime.now()
print(f"Current time: {now:%Y-%m-%d %H:%M:%S}")
print(f"Date only: {now:%B %d, %Y}")

# Number formatting
large_number = 1234567.89
print(f"With commas: {large_number:,.2f}")
print(f"Scientific notation: {large_number:.2e}")
print(f"As percentage: {0.75:.1%}")

print("\n=== PRACTICAL FORMATTING EXAMPLES ===")
# Report generation
students = [
    ("Alice Johnson", 95.6, "A"),
    ("Bob Smith", 87.3, "B"),
    ("Charlie Brown", 92.1, "A-")
]

print("STUDENT GRADE REPORT")
print("-" * 40)
print(f"{'Name':<15} {'Score':<8} {'Grade':<5}")
print("-" * 40)

for student_name, score, grade in students:
    print(f"{student_name:<15} {score:<8.1f} {grade:<5}")

# Invoice formatting
items = [
    ("Widget A", 2, 15.99),
    ("Widget B", 1, 25.50),
    ("Widget C", 3, 8.75)
]

print("\n" + "="*50)
print("INVOICE")
print("="*50)
print(f"{'Item':<12} {'Qty':<5} {'Price':<8} {'Total':<8}")
print("-" * 50)

total_amount = 0
for item, qty, price in items:
    item_total = qty * price
    total_amount += item_total
    print(f"{item:<12} {qty:<5} ${price:<7.2f} ${item_total:<7.2f}")

print("-" * 50)
print(f"{'TOTAL:':<12} {'':>25} ${total_amount:.2f}")
