# string_indexing_slicing.py - Advanced string manipulation

# String indexing examples
text = "Python Programming"
print("=== STRING INDEXING ===")
print(f"Text: '{text}'")
print(f"Length: {len(text)}")
print(f"First character: text[0] = '{text[0]}'")
print(f"Last character: text[-1] = '{text[-1]}'")
print(f"Second last: text[-2] = '{text[-2]}'")
print(f"Character at index 7: text[7] = '{text[7]}'")

# String slicing examples
print("\n=== STRING SLICING ===")
print(f"First 6 characters: text[:6] = '{text[:6]}'")
print(f"Last 11 characters: text[7:] = '{text[7:]}'")
print(f"Middle part: text[3:10] = '{text[3:10]}'")
print(f"Every 2nd character: text[::2] = '{text[::2]}'")
print(f"Reverse string: text[::-1] = '{text[::-1]}'")
print(f"Last 5 reversed: text[:-6:-1] = '{text[:-6:-1]}'")

# Practical slicing examples
print("\n=== PRACTICAL EXAMPLES ===")

# Extract file extension
filename = "document.pdf"
extension = filename[filename.rfind('.') + 1:]
print(f"File: {filename}, Extension: {extension}")

# Extract domain from email
email = "user@example.com"
domain = email[email.find('@') + 1:]
print(f"Email: {email}, Domain: {domain}")

# Extract initials
full_name = "John Doe Smith"
words = full_name.split()
initials = ''.join([word[0] for word in words])
print(f"Name: {full_name}, Initials: {initials}")

# Validate credit card (show only last 4 digits)
credit_card = "1234567890123456"
masked = "*" * (len(credit_card) - 4) + credit_card[-4:]
print(f"Credit Card: {masked}")

# Extract area code from phone number
phone = "(555) 123-4567"
area_code = phone[1:4]  # Extract from position 1 to 3
print(f"Phone: {phone}, Area Code: {area_code}")
