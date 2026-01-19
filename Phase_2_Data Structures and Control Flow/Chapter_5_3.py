# elif_demo.py - Multiple conditions
# Grade calculator with elif
score = float(input("Enter your score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70: 
    grade = "C"
elif score >= 60:
    grade = "D" 
else:
    grade = "F"

print(f"Your grade is: {grade}")

# Season detector
month = int(input("Enter month number (1-12): "))

if month in [12, 1, 2]:
    season = "Winter"
elif month in [3, 4, 5]:
    season = "Spring"
elif month in [6, 7, 8]:
    season = "Summer"
elif month in [9, 10, 11]:
    season = "Fall"
else:
    season = "Invalid month"

print(f"The season is: {season}")

# Traffic light system
light = input("Enter traffic light color (red/yellow/green): ").lower()

if light == "red":
    print("Stop!")
elif light == "yellow":
    print("Caution! Prepare to stop.")
elif light == "green":
    print("Go!")
else:
    print("Invalid traffic light color")
