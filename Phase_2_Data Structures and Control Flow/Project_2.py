# project2_atm_system.py - Banking system with control flow

class ATMSystem:
    def __init__(self):
        # Sample accounts database
        self.accounts = {
            "1234": {"name": "John Doe", "pin": "1111", "balance": 1500.00},
            "5678": {"name": "Jane Smith", "pin": "2222", "balance": 2300.50},
            "9012": {"name": "Bob Johnson", "pin": "3333", "balance": 750.75}
        }
        self.current_account = None
        self.max_attempts = 3

    def display_welcome(self):
        """Display welcome message"""
        print("\n" + "=" * 40)
        print("    WELCOME TO PYTHON BANK ATM")
        print("=" * 40)

    def authenticate_user(self):
        """Authenticate user with account number and PIN"""
        attempts = 0

        while attempts < self.max_attempts:
            account_number = input("\nEnter account number: ")

            if account_number in self.accounts:
                pin = input("Enter PIN: ")

                if self.accounts[account_number]["pin"] == pin:
                    self.current_account = account_number
                    print(f"\nWelcome, {self.accounts[account_number]['name']}!")
                    return True
                else:
                    attempts += 1
                    remaining = self.max_attempts - attempts
                    if remaining > 0:
                        print(f"Invalid PIN. {remaining} attempts remaining.")
                    else:
                        print("Account locked due to too many failed attempts.")
            else:
                attempts += 1
                remaining = self.max_attempts - attempts
                if remaining > 0:
                    print(f"Account not found. {remaining} attempts remaining.")
                else:
                    print("Access denied.")

        return False

    def display_menu(self):
        """Display main menu options"""
        print("\n" + "-" * 30)
        print("ATM MENU")
        print("-" * 30)
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")
        print("-" * 30)

    def check_balance(self):
        """Display current balance"""
        balance = self.accounts[self.current_account]["balance"]
        print(f"\nCurrent Balance: ${balance:.2f}")

    def deposit_money(self):
        """Handle money deposit"""
        while True:
            try:
                amount = float(input("Enter deposit amount: $"))
                if amount <= 0:
                    print("Please enter a positive amount.")
                    continue
                elif amount > 10000:
                    print("Maximum deposit limit is $10,000.")
                    continue
                else:
                    self.accounts[self.current_account]["balance"] += amount
                    new_balance = self.accounts[self.current_account]["balance"]
                    print(f"${amount:.2f} deposited successfully!")
                    print(f"New balance: ${new_balance:.2f}")
                    break
            except ValueError:
                print("Please enter a valid amount.")

    def withdraw_money(self):
        """Handle money withdrawal"""
        while True:
            try:
                amount = float(input("Enter withdrawal amount: $"))
                current_balance = self.accounts[self.current_account]["balance"]

                if amount <= 0:
                    print("Please enter a positive amount.")
                    continue
                elif amount > current_balance:
                    print(f"Insufficient funds. Available: ${current_balance:.2f}")
                    continue
                elif amount > 500:
                    print("Daily withdrawal limit is $500.")
                    continue
                else:
                    self.accounts[self.current_account]["balance"] -= amount
                    new_balance = self.accounts[self.current_account]["balance"]
                    print(f"${amount:.2f} withdrawn successfully!")
                    print(f"Remaining balance: ${new_balance:.2f}")
                    break
            except ValueError:
                print("Please enter a valid amount.")

    def transaction_history(self):
        """Display mock transaction history"""
        print("\n" + "-" * 40)
        print("RECENT TRANSACTIONS")
        print("-" * 40)

        # Mock transaction data
        transactions = [
            ("2024-01-15", "Deposit", "+$500.00"),
            ("2024-01-14", "Withdrawal", "-$200.00"),
            ("2024-01-13", "Deposit", "+$1000.00"),
            ("2024-01-12", "Withdrawal", "-$50.00")
        ]

        for date, transaction_type, amount in transactions:
            print(f"{date} | {transaction_type:<12} | {amount}")

        print("-" * 40)

    def run(self):
        """Main ATM operation loop"""
        self.display_welcome()

        if not self.authenticate_user():
            print("Goodbye!")
            return

        while True:
            self.display_menu()

            try:
                choice = input("Enter your choice (1-5): ")

                if choice == "1":
                    self.check_balance()
                elif choice == "2":
                    self.deposit_money()
                elif choice == "3":
                    self.withdraw_money()
                elif choice == "4":
                    self.transaction_history()
                elif choice == "5":
                    print("\nThank you for using Python Bank ATM!")
                    print("Have a great day!")
                    break
                else:
                    print("Invalid choice. Please select 1-5.")

                # Ask if user wants to continue
                if choice in ["1", "2", "3", "4"]:
                    continue_choice = input("\nPerform another transaction? (y/n): ")
                    if continue_choice.lower() != 'y':
                        print("\nThank you for using Python Bank ATM!")
                        break

            except KeyboardInterrupt:
                print("\n\nTransaction cancelled. Goodbye!")
                break


# Run the ATM system
if __name__ == "__main__":
    atm = ATMSystem()
    atm.run()
