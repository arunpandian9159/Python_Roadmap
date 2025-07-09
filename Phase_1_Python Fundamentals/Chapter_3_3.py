#Python reserved keywords

import keyword

# Display all Python keywords
print("Python Keywords:")
for i, kw in enumerate(keyword.kwlist, 1):
    print(f"{i:2d}. {kw}")

# Examples of keyword usage
def demonstrate_keywords():
    # Control flow keywords
    if True:
        print("\nif keyword in action")
    elif False:
        print("elif keyword")
    else:
        print("else keyword")

    # Loop keywords
    for i in range(3):
        if i == 1:
            continue  # Skip this iteration
        print(f"for loop: {i}")

    # Function definition keywords
    def inner_function():
        return "Function defined with def keyword"

    return inner_function()

print(f"{demonstrate_keywords()}")
