# if_statement_demo.py - Conditional logic

# Basic if statement
age = 18
if age >= 18:
    print("You are eligible to vote!")

# Multiple conditions
temperature = 25
if temperature > 30:
    print("It's hot outside!")
if temperature < 10:
    print("It's cold outside!")
if 10 <= temperature <= 30:
    print("The weather is pleasant!")

# Checking user input
user_input = input("Enter your grade (A, B, C, D, F): ").upper()
if user_input == "A":
    print("Excellent work!")
if user_input in ["B", "C"]:
    print("Good job!")
if user_input in ["D", "F"]:
    print("You need to study more!")
