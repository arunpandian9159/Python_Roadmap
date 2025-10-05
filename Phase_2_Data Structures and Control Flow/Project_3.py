# project3_contact_manager.py - Advanced function usage

import json
import os
from datetime import datetime

class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()
    def load_contacts(self):
        """Load contacts from file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                print("Error loading contacts. Starting with empty list.")
                return []
        return []

    def save_contacts(self):
        """Save contacts to file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.contacts, file, indent=2)
            return True
        except Exception as e:
            print(f"Error saving contacts: {e}")
            return False
    def add_contact(self, name, phone, email, category="Personal"):
        """Add a new contact"""

        # Validation functions
        def validate_phone(phone):
            digits = ''.join(filter(str.isdigit, phone))
            return len(digits) >= 10

        def validate_email(email):
            return '@' in email and '.' in email.split('@')[1]

        # Validate input
        if not name.strip():
            return False, "Name cannot be empty"

        if not validate_phone(phone):
            return False, "Phone number must have at least 10 digits"

        if not validate_email(email):
            return False, "Invalid email format"

        # Check for duplicates
        if any(contact['name'].lower() == name.lower() for contact in self.contacts):
            return False, "Contact with this name already exists"

        # Create contact
        contact = {
            "id": len(self.contacts) + 1,
            "name": name.strip(),
            "phone": phone.strip(),
            "email": email.strip().lower(),
            "category": category,
            "created_date": datetime.now().isoformat(),
            "updated_date": datetime.now().isoformat()
        }

        self.contacts.append(contact)
        self.save_contacts()
        return True, f"Contact '{name}' added successfully"

    def search_contacts(self, query):
        """Search contacts by name, phone, or email"""
        query = query.lower()
        results = []

        for contact in self.contacts:
            if (query in contact['name'].lower() or
                    query in contact['phone'] or
                    query in contact['email']):
                results.append(contact)

        return results

    def update_contact(self, contact_id, **updates):
        """Update an existing contact"""
        contact = self.find_contact_by_id(contact_id)

        if not contact:
            return False, "Contact not found"

        # Update fields
        for field, value in updates.items():
            if field in ['name', 'phone', 'email', 'category']:
                contact[field] = value

        contact['updated_date'] = datetime.now().isoformat()
        self.save_contacts()
        return True, "Contact updated successfully"

    def delete_contact(self, contact_id):
        """Delete a contact"""
        contact = self.find_contact_by_id(contact_id)

        if not contact:
            return False, "Contact not found"

        self.contacts.remove(contact)
        self.save_contacts()
        return True, f"Contact '{contact['name']}' deleted"

    def find_contact_by_id(self, contact_id):
        """Find contact by ID"""
        return next((c for c in self.contacts if c['id'] == contact_id), None)

    def get_contacts_by_category(self, category):
        """Get all contacts in a specific category"""
        return [c for c in self.contacts if c['category'].lower() == category.lower()]

    def get_statistics(self):
        """Get contact statistics"""
        categories = {}
        for contact in self.contacts:
            category = contact['category']
            categories[category] = categories.get(category, 0) + 1

        return {
            "total_contacts": len(self.contacts),
            "categories": categories,
            "latest_contact": max(self.contacts, key=lambda x: x['created_date'])['name'] if self.contacts else "None"
        }

    def export_contacts(self, format_type="csv"):
        """Export contacts to different formats"""
        if not self.contacts:
            return False, "No contacts to export"

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        if format_type.lower() == "csv":
            filename = f"contacts_export_{timestamp}.csv"
            try:
                with open(filename, 'w') as file:
                    # Write header
                    file.write("ID,Name,Phone,Email,Category,Created Date\n")

                    # Write data
                    for contact in self.contacts:
                        file.write(f"{contact['id']},{contact['name']},{contact['phone']},"
                                   f"{contact['email']},{contact['category']},{contact['created_date']}\n")

                return True, f"Contacts exported to {filename}"
            except Exception as e:
                return False, f"Export failed: {e}"

        return False, "Unsupported format"

    def display_contacts(self, contacts=None):
        """Display contacts in a formatted table"""
        if contacts is None:
            contacts = self.contacts

        if not contacts:
            print("No contacts found.")
            return

        # Table formatting
        print("\n" + "=" * 80)
        print(f"{'ID':<4} {'Name':<20} {'Phone':<15} {'Email':<25} {'Category':<12}")
        print("=" * 80)

        for contact in contacts:
            print(f"{contact['id']:<4} {contact['name']:<20} {contact['phone']:<15} "
                  f"{contact['email']:<25} {contact['category']:<12}")

        print("=" * 80)
        print(f"Total: {len(contacts)} contact(s)")


def main():
    """Main program loop"""
    manager = ContactManager()

    # Lambda functions for menu operations
    menu_options = {
        "1": lambda: add_contact_interactive(manager),
        "2": lambda: view_all_contacts(manager),
        "3": lambda: search_contacts_interactive(manager),
        "4": lambda: update_contact_interactive(manager),
        "5": lambda: delete_contact_interactive(manager),
        "6": lambda: view_statistics(manager),
        "7": lambda: export_contacts_interactive(manager),
        "8": lambda: print("Goodbye!")
    }

    def display_menu():
        print("\n" + "=" * 50)
        print("           CONTACT MANAGER")
        print("=" * 50)
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Statistics")
        print("7. Export Contacts")
        print("8. Exit")
        print("=" * 50)

    def add_contact_interactive(manager):
        print("\n--- Add New Contact ---")
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        category = input("Category (Personal/Work/Family): ") or "Personal"

        success, message = manager.add_contact(name, phone, email, category)
        print(f"{'✓' if success else '✗'} {message}")

    def view_all_contacts(manager):
        print("\n--- All Contacts ---")
        manager.display_contacts()

    def search_contacts_interactive(manager):
        print("\n--- Search Contacts ---")
        query = input("Enter search term (name/phone/email): ")
        results = manager.search_contacts(query)

        if results:
            print(f"\nFound {len(results)} result(s):")
            manager.display_contacts(results)
        else:
            print("No contacts found.")

    def update_contact_interactive(manager):
        print("\n--- Update Contact ---")
        try:
            contact_id = int(input("Enter contact ID: "))
            contact = manager.find_contact_by_id(contact_id)

            if not contact:
                print("Contact not found.")
                return

            print(f"Current contact: {contact['name']}")
            updates = {}

            # Get updates
            new_name = input(f"Name ({contact['name']}): ")
            if new_name: updates['name'] = new_name

            new_phone = input(f"Phone ({contact['phone']}): ")
            if new_phone: updates['phone'] = new_phone

            new_email = input(f"Email ({contact['email']}): ")
            if new_email: updates['email'] = new_email

            new_category = input(f"Category ({contact['category']}): ")
            if new_category: updates['category'] = new_category

            if updates:
                success, message = manager.update_contact(contact_id, **updates)
                print(f"{'✓' if success else '✗'} {message}")
            else:
                print("No changes made.")

        except ValueError:
            print("Invalid contact ID.")

    def delete_contact_interactive(manager):
        print("\n--- Delete Contact ---")
        try:
            contact_id = int(input("Enter contact ID: "))
            contact = manager.find_contact_by_id(contact_id)

            if not contact:
                print("Contact not found.")
                return

            confirm = input(f"Delete '{contact['name']}'? (y/N): ")
            if confirm.lower() == 'y':
                success, message = manager.delete_contact(contact_id)
                print(f"{'✓' if success else '✗'} {message}")
            else:
                print("Deletion cancelled.")

        except ValueError:
            print("Invalid contact ID.")

    def view_statistics(manager):
        print("\n--- Contact Statistics ---")
        stats = manager.get_statistics()

        print(f"Total Contacts: {stats['total_contacts']}")
        print(f"Latest Contact: {stats['latest_contact']}")
        print("\nContacts by Category:")

        for category, count in stats['categories'].items():
            print(f"  {category}: {count}")

    def export_contacts_interactive(manager):
        print("\n--- Export Contacts ---")
        format_type = input("Export format (csv): ") or "csv"
        success, message = manager.export_contacts(format_type)
        print(f"{'✓' if success else '✗'} {message}")

    # Main program loop
    while True:
        display_menu()
        choice = input("Choose an option (1-8): ")

        if choice in menu_options:
            menu_options[choice]()
            if choice == "8":
                break
        else:
            print("Invalid choice. Please try again.")

        if choice != "8":
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
