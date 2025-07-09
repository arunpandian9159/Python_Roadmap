#Creating a custom module
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b, c):
    return a - b - c

PI = 3.14159

if __name__ == "__main__":
    print(f"5 + 2 = {add(5, 2)}")
    print(f"4 * 6 = {multiply(4, 6)}")
    print(f"5 - 2 - 3 = {subtract(5,2,4)}")
