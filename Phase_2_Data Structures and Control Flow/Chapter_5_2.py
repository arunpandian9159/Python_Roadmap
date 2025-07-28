# if_else_demo.py - Binary decisions
# Basic if-else
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Password checker
password = input("Enter password: ")
if len(password) >= 8:
    print("Password is strong enough")
else:
    print("Password is too short (minimum 8 characters)")

# Age category
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor")
else:
    print("You are an adult")

# Grade calculator
score = float(input("Enter your score (0-100): "))
if score >= 60:
    print("You passed!")
else:
    print("You failed. Better luck next time!")
