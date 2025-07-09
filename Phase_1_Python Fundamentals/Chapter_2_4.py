#Understanding package management

# First, install a package using pip in terminal:
# pip install requests

try:
    import requests

    print("✓ requests library is installed")

    # Example usage of installed package
    response = requests.get("https://httpbin.org/json")
    if response.status_code == 200:
        print("✓ Successfully made HTTP request")
    else:
        print("✗ Request failed")

except ImportError:
    print("✗ requests library not installed")
    print("Run: pip install requests")
