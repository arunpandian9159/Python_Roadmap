#Combining all data types
class PersonalInfoManager:
    def __init__(self):
        # Using different data types
        self.contacts = {}  # Dictionary
        self.favorite_numbers = set()  # Set
        self.important_dates = []  # List
        self.personal_info = ()  # Tuple (immutable)
        self.is_initialized = True  # Boolean
    def add_contact(self, name, phone, email):
        """Add a new contact"""
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'added_date': self.get_current_date()
        }
        print(f"✓ Contact '{name}' added successfully")
 
    def add_favorite_number(self, number):
        """Add a favorite number (no duplicates)"""
        self.favorite_numbers.add(number)
        print(f"✓ Number {number} added to favorites")
    def add_important_date(self, event, date):
        """Add an important date"""
        self.important_dates.append((event, date))
        print(f"✓ Important date added: {event} on {date}")

    def set_personal_info(self, name, age, city):
        """Set personal information (immutable once set)"""
        self.personal_info = (name, age, city)
        print(f"✓ Personal info set for {name}")

    def get_current_date(self):
        """Get current date as string"""
        import datetime
        return datetime.datetime.now().strftime("%Y-%m-%d")

    def display_summary(self):
        """Display all information"""
        print("\n" + "=" * 50)
        print("PERSONAL INFORMATION MANAGER SUMMARY")
        print("=" * 50)

        # Personal info (tuple)
        if self.personal_info:
            name, age, city = self.personal_info
            print(f"Name: {name}, Age: {age}, City: {city}")

        # Contacts (dictionary)
        print(f"\nContacts ({len(self.contacts)}):")
        for name, info in self.contacts.items():
            print(f"  {name}: {info['phone']} | {info['email']}")

        # Favorite numbers (set)
        print(f"\nFavorite Numbers: {sorted(self.favorite_numbers)}")

        # Important dates (list)
        print(f"\nImportant Dates ({len(self.important_dates)}):")
        for event, date in self.important_dates:
            print(f"  {event}: {date}")


# Example usage
if __name__ == "__main__":
    # Create manager
    manager = PersonalInfoManager()

    # Set personal information
    manager.set_personal_info("John Doe", 25, "New York")

    # Add contacts
    manager.add_contact("Alice Smith", "555-0101", "alice@email.com")
    manager.add_contact("Bob Johnson", "555-0102", "bob@email.com")

    # Add favorite numbers
    manager.add_favorite_number(7)
    manager.add_favorite_number(42)
    manager.add_favorite_number(7)  # Duplicate will be ignored

    # Add important dates
    manager.add_important_date("Birthday", "1998-05-15")
    manager.add_important_date("Graduation", "2020-06-01")

    # Display summary
    manager.display_summary()
