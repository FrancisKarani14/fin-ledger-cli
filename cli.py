import click
from auth import login, signup, get_current_user, require_login, logout
from crud import deposit, withdraw

while True:
    click.secho("\nFinance Ledger CLI", fg="blue", bold=True)

    if get_current_user():
        click.secho("Logged in as: " +
                    get_current_user().username, fg="yellow")

    click.secho("1. Login", fg="green")
    click.secho("2. Signup", fg="green")
    click.secho("3. Deposit", fg="green")
    click.secho("4. Withdraw", fg="green")
    click.secho("5. Logout", fg="cyan")
    click.secho("6. Exit", fg="red")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            login(username, password)

        elif choice == "2":
            username = input("Username: ")
            email = input("Email: ")
            password = input("Password: ")
            signup(username, email, password)

        elif choice == "3":
            require_login()
            user = get_current_user()

            amount = input("Amount to deposit: ")
            description = input("Description (optional): ")
            deposit(user.wallet.id, amount, description)

        elif choice == "4":
            require_login()
            user = get_current_user()

            amount = input("Amount to withdraw: ")
            description = input("Description (optional): ")
            withdraw(user.wallet.id, amount, description)

        elif choice == "5":
            logout()

        elif choice == "6":
            click.secho("Goodbye 👋", fg="cyan")
            break

        else:
            click.secho("Invalid choice", fg="red")

    except PermissionError as e:
        click.secho(str(e), fg="red")

    except Exception as e:
        click.secho(f"Error: {e}", fg="red")
