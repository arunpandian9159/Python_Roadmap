# variable_scope_demo.py - Understanding variable scope

# Global variable
global_var = "I'm a global variable"
count = 0


def demonstrate_local_scope():
    """Demonstrate local variable scope"""
    local_var = "I'm a local variable"
    print(f"Inside function: {local_var}")
    print(f"Inside function can access global: {global_var}")


def demonstrate_global_keyword():
    """Demonstrate global keyword usage"""
    global count
    count += 1  # Modify global variable
    print(f"Count incremented to: {count}")


def demonstrate_local_override():
    """Demonstrate local variable overriding global"""
    global_var = "I'm a local variable with same name"
    print(f"Local override: {global_var}")


def outer_function():
    """Demonstrate nested function scope"""
    outer_var = "I'm in outer function"

    def inner_function():
        """Inner function with access to outer scope"""
        inner_var = "I'm in inner function"
        print(f"Inner can access: {outer_var}")
        print(f"Inner variable: {inner_var}")

    inner_function()
    print(f"Outer variable: {outer_var}")
    # print(inner_var)  # This would cause an error


def demonstrate_nonlocal():
    """Demonstrate nonlocal keyword"""
    counter = 0

    def increment():
        nonlocal counter  # Modify outer function variable
        counter += 1
        return counter

    print(f"Initial counter: {counter}")
    print(f"After increment: {increment()}")
    print(f"After another increment: {increment()}")
    return counter


# LEGB Rule demonstration (Local, Enclosing, Global, Built-in)
x = "global x"


def legb_demo():
    x = "enclosing x"

    def inner():
        x = "local x"
        print(f"LEGB - Local: {x}")
        print(f"LEGB - Built-in len: {len}")  # Built-in function

    inner()
    print(f"LEGB - Enclosing: {x}")


# Variable scope examples
print("=== LOCAL SCOPE ===")
demonstrate_local_scope()
# print(local_var)  # This would cause NameError

print("\n=== GLOBAL KEYWORD ===")
print(f"Initial count: {count}")
demonstrate_global_keyword()
demonstrate_global_keyword()
print(f"Final count: {count}")

print("\n=== LOCAL OVERRIDE ===")
print(f"Global variable: {global_var}")
demonstrate_local_override()
print(f"After function call: {global_var}")  # Still original value

print("\n=== NESTED FUNCTIONS ===")
outer_function()

print("\n=== NONLOCAL KEYWORD ===")
final_counter = demonstrate_nonlocal()
print(f"Returned counter: {final_counter}")

print("\n=== LEGB RULE ===")
print(f"Global x: {x}")
legb_demo()
print(f"Still global x: {x}")

# Practical scope example - Configuration management
print("\n=== PRACTICAL EXAMPLE ===")

# Global configuration
config = {
    "debug": False,
    "version": "1.0",
    "max_users": 100
}


def update_config(key, value):
    """Update global configuration"""
    global config
    old_value = config.get(key, "Not set")
    config[key] = value
    print(f"Config updated: {key} = {old_value} → {value}")

def get_config(key):
    """Get configuration value"""
    return config.get(key, "Not found")


def create_user_session():
    """Create user session with local variables"""
    session_id = "sess_12345"
    user_data = {"name": "Alice", "role": "user"}

    def validate_permissions():
        """Check permissions using enclosing scope"""
        max_users = config["max_users"]  # Global access
        current_users = 50  # Local to this function

        if current_users < max_users:
            print(f"Session {session_id} validated for {user_data['name']}")
            return True
        else:
            print("Maximum users reached")
            return False

    return validate_permissions()


print("Initial config:", config)
update_config("debug", True)
update_config("theme", "dark")
print("Updated config:", config)

print("\nCreating user session:")
session_valid = create_user_session()
print(f"Session valid: {session_valid}")
