# nested_if_demo.py - Complex conditional logic
# Login system
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "secret123":
        print("Welcome, Administrator!")
        if input("Access admin panel? (y/n): ").lower() == "y":
            print("Opening admin panel...")
        else: 
            print("Staying in main area")
    else:
        print("Invalid admin password")
elif username == "user":
    if password == "user123":
        print("Welcome, User!")
    else:
        print("Invalid user password")
else:
    print("Username not found")

# Number analysis
number = float(input("Enter a number: "))

if number > 0:
    print("Number is positive")
    if number > 100:
        print("Number is also greater than 100")
        if number > 1000:
            print("Number is very large!")
    else:
        print("Number is small to medium")
elif number < 0:
    print("Number is negative")
    if number < -100:
        print("Number is very negative!")
else:
    print("Number is zero")

# Shopping discount calculator
total_amount = float(input("Enter total purchase amount: $"))
is_member = input("Are you a member? (y/n): ").lower() == "y"

if total_amount > 100:
    if is_member:
        discount = 0.20  # 20% for members
        print("You get a 20% member discount!")
    else:
        discount = 0.10  # 10% for non-members
        print("You get a 10% discount!")

    final_amount = total_amount * (1 - discount)
    print(f"Final amount: ${final_amount:.2f}")
else:
    if is_member:
        discount = 0.05  # 5% for members on small purchases
        final_amount = total_amount * 0.95
        print(f"Small member discount applied. Final: ${final_amount:.2f}")
    else:
        print(f"No discount applied. Total: ${total_amount:.2f}")
