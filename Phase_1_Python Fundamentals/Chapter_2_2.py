#Using built-in and custom modules
import math
import random
from Chapter_2_1 import add, PI

# Built-in module usage
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Random number: {random.randint(1, 100)}")

# Custom module usage
result = add(10, 20)
print(f"Using custom module: 10 + 20 = {result}")
print(f"Value of PI: {PI}")
