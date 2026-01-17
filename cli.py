import click
from crud import deposit, withdraw
from auth import login, signup

# main loop
while True:
    click.secho("\nWelcome to Finance Ledger CLI", fg="blue", bold=True)
    click.secho("1. Login", fg="green")
    click.secho("2. signup", fg="green")
    click.secho("3. Deposit", fg="green")
    click.secho("4. Withdraw", fg="green")
    click.secho("5. Exit", fg="red")

    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        login(username, password)

    elif choice == "2":
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        signup(username, email, password)

    elif choice == "3":
        amount = input("Enter amount to deposit: ")
        description = input("Enter description (optional): ")
        deposit(amount, description)

    elif choice == "4":
        amount = input("Enter amount to withdraw: ")
        description = input("Enter description (optional): ")
        withdraw(amount, description)

    elif choice == "5":
        click.secho("Goodbye!", fg="cyan")   
        break
    else:
        click.secho("Invalid choice. Please try again.")

