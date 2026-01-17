import click

from crud import (
add_user,
create_account,
deposite, withdraw, delete_account
)

# main menu

while True:
    print("\nPersonal Ledger CLI")
    print("1. Add User")
    print("2. Create Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Delete Account")
    print("6. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        username = input("Username: ")
        email = input("Email: ")
        password = input("Password: ")
        is_admin = input("Is Admin (y/n): ").lower() == 'y'
        add_user(username, email, password, is_admin)

    elif choice == "2":
        user_id = int(input("User ID: "))
        account_name = input("Account Name: ")
        initial_balance = float(input("Initial Balance (default 0): ") or 0)
        create_account(user_id, account_name, initial_balance)

    elif choice == "3":
        account_id = int(input("Account ID: "))
        amount = float(input("Amount to Deposit: "))
        description = input("Description (optional): ")
        deposite(account_id, amount, description)

    elif choice == "4":
        account_id = int(input("Account ID: "))
        amount = float(input("Amount to Withdraw: "))
        description = input("Description (optional): ")
        withdraw(account_id, amount, description)

    elif choice == "5":
        account_id = int(input("Account ID to Delete: "))
        delete_account(account_id)

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid option. Please try again.")