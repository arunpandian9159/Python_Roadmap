# while_loop_demo.py - Repetitive execution with condition
# Basic while loop - counting
print("=== COUNTING WITH WHILE LOOP ===")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# Sum of numbers
print("\n=== SUM CALCULATION ===")
number = 1
total = 0
while number <= 10:
    total += number
    number += 1
print(f"Sum of numbers 1-10: {total}")

# User input validation
print("\n=== INPUT VALIDATION ===")
password = ""
while len(password) < 6:
    password = input("Enter password (minimum 6 characters): ")
    if len(password) < 6:
        print("Password too short!")
print("Password accepted!")

# Guessing game
print("\n=== GUESSING GAME ===")
import random

secret_number = random.randint(1, 10)
guess = 0
attempts = 0

while guess != secret_number:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You won in {attempts} attempts!")

# Menu system
print("\n=== MENU SYSTEM ===")
choice = ""
while choice != "quit":
    print("\nOptions: 1. Hello 2. Time 3. Quit")
    choice = input("Enter choice: ").lower()

    if choice == "1":
        print("Hello, World!")
    elif choice == "2":
        import datetime

        print(f"Current time: {datetime.datetime.now()}")
    elif choice == "quit":
        print("Goodbye!")
    else:
        print("Invalid choice!")
