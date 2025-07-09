#Your first Python program
print("Hello, World!")
print("Welcome to Python programming!")

# This demonstrates basic output functionality
# The print() function displays text to the console

print("=============================================================================================================")
#Showcasing Python's key features

# 1. Simple and readable syntax
name = "Python"
version = 3.11

# 2. Dynamic typing (no need to declare variable types)
number = 42          # Integer
price = 99.99        # Float
message = "Hello"    # String
is_active = True     # Boolean

# 3. Cross-platform compatibility
import platform
print(f"\nRunning on: {platform.system()}")

# 4. Extensive standard library
import datetime
current_time = datetime.datetime.now()
print(f"Current time: {current_time}")

print("=============================================================================================================")
#Real-world Python applications

# Web Development Example
print("\n=== WEB DEVELOPMENT ===")
print("Flask/Django for web applications")

# Data Science Example
print("=== DATA SCIENCE ===")
numbers = [1, 2, 3, 4, 5]
average = sum(numbers) / len(numbers)
print(f"Average of {numbers} = {average}")

# Automation Example
print("=== AUTOMATION ===")
import os
files = os.listdir(".")
print(f"Files in current directory: {len(files)}")

print("=============================================================================================================")

