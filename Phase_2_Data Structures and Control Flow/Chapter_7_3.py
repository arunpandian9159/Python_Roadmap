# string_operations.py - Essential string methods and operations
# Sample text for demonstrations
text = "  Python Programming is Amazing!  "
sample_text = "Hello, World! Welcome to Python Programming."

print("=== STRING CLEANING ===")
print(f"Original: '{text}'")
print(f"Stripped: '{text.strip()}'")
print(f"Left strip: '{text.lstrip()}'")
print(f"Right strip: '{text.rstrip()}'")
print("\n=== CASE OPERATIONS ===")
print(f"Original: {sample_text}") 
print(f"Upper: {sample_text.upper()}")
print(f"Lower: {sample_text.lower()}")
print(f"Title: {sample_text.title()}")
print(f"Capitalize: {sample_text.capitalize()}") 
print(f"Swap case: {sample_text.swapcase()}")

print("\n=== STRING TESTING ===")
test_strings = ["Hello123", "12345", "hello", "HELLO", "Hello World"]
for test_str in test_strings:
    print(f"\nTesting: '{test_str}'") 
    print(f"  isalnum(): {test_str.isalnum()}")
    print(f"  isdigit(): {test_str.isdigit()}")
    print(f"  isalpha(): {test_str.isalpha()}")
    print(f"  islower(): {test_str.islower()}")
    print(f"  isupper(): {test_str.isupper()}")
    print(f"  istitle(): {test_str.istitle()}")

print("\n=== SEARCH AND FIND ===")
sentence = "Python is powerful, Python is easy, Python is fun!"
print(f"Sentence: {sentence}")
print(f"Count 'Python': {sentence.count('Python')}")
print(f"Find 'is': {sentence.find('is')}")
print(f"Find 'Java': {sentence.find('Java')}")  # Returns -1 if not found
print(f"Index 'powerful': {sentence.index('powerful')}")
print(f"Starts with 'Python': {sentence.startswith('Python')}")
print(f"Ends with 'fun!': {sentence.endswith('fun!')}")

print("\n=== STRING REPLACEMENT ===")
original = "I love Java programming. Java is great!"
print(f"Original: {original}")
print(f"Replace Java with Python: {original.replace('Java', 'Python')}")
print(f"Replace first Java only: {original.replace('Java', 'Python', 1)}")

print("\n=== STRING SPLITTING AND JOINING ===")
csv_data = "apple,banana,orange,grape"
words = "Python is awesome"

print(f"CSV data: {csv_data}")
fruits = csv_data.split(',')
print(f"Split by comma: {fruits}")

print(f"\nWords: {words}")
word_list = words.split()
print(f"Split by space: {word_list}")
print(f"Join with ' | ': {' | '.join(word_list)}")
print(f"Join with newlines:\n{chr(10).join(word_list)}")

print("\n=== ADVANCED STRING OPERATIONS ===")
# String translation (character mapping)
text = "Hello, World!"
translation_table = str.maketrans("aeiou", "12345")
translated = text.translate(translation_table)
print(f"Original: {text}")
print(f"Vowels to numbers: {translated}")

# Padding and centering
word = "Python"
print(f"\nWord: '{word}'")
print(f"Left pad with zeros: '{word.ljust(10, '0')}'")
print(f"Right pad with dashes: '{word.rjust(10, '-')}'")
print(f"Center with stars: '{word.center(12, '*')}'")
print(f"Zero fill: '{word.zfill(10)}'")

# Partition and split
email = "user@domain.com"
username, separator, domain = email.partition('@')
print(f"\nEmail: {email}")
print(f"Username: {username}, Domain: {domain}")

# String encoding/decoding
text = "Hello, 世界!"
encoded = text.encode('utf-8')
decoded = encoded.decode('utf-8')
print(f"\nOriginal: {text}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")
