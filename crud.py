from models import User, Account, Transaction, Session, TransactionType

def add_user(username, email, password_hash, is_admin=False):
    session = Session()
    try:
        new_user = User(
            username=username,
            email=email,
            password_hash=password_hash,
            is_admin=is_admin
        )
        session.add(new_user)
        session.commit()
        print(f"User {username} added successfully.")
    except Exception as e:
        print(f"Error adding user: {e}")
        session.rollback()
    finally:
        session.close()


def create_account(user_id, account_name, initial_balance=0):
    session = Session()
    try:
        new_account = Account(
            user_id=user_id,
            account_name=account_name,
            balance=initial_balance
        )
        session.add(new_account)
        session.commit()
        print(f"Account {account_name} created successfully.")
    except Exception as e:
        print(f"Error creating account: {e}")
        session.rollback()
    finally:
        session.close()

def deposite(account_id, amount, description=""):
    session = Session()
    try:
        account = session.get(Account, account_id)
        if account:
            new_transaction = Transaction(
                account_id=account_id,
                type=TransactionType.deposit,
                amount=amount,
                description=description
            )
            account.balance += amount
            session.add(new_transaction)
            session.commit()
            print(f"Deposited {amount} to account {account_id}.")
        else:
            print(f"Account {account_id} not found.")
    except Exception as e:
        print(f"Error during deposit: {e}")
        session.rollback()
    finally:
        session.close()

def withdraw(account_id, amount, description=""):
    session = Session()
    try:
        account = session.get(Account, account_id)
        if account:
            if account.balance >= amount:
                new_transaction = Transaction(
                    account_id=account_id,
                    type=TransactionType.withdrawal,
                    amount=amount,
                    description=description
                )
                account.balance -= amount
                session.add(new_transaction)
                session.commit()
                print(f"Withdrew {amount} from account {account_id}.")
            else:
                print(f"Insufficient funds in account {account_id}.")
        else:
            print(f"Account {account_id} not found.")
    except Exception as e:
        print(f"Error during withdrawal: {e}")
        session.rollback()
    finally:
        session.close()

def delete_account(account_id):
    session = Session()
    try:
        account = session.get(Account, account_id)
        if account:
            session.delete(account)
            session.commit()
            print(f"Account {account_id} deleted successfully.")
        else:
            print(f"Account {account_id} not found.")
    except Exception as e:
        print(f"Error deleting account: {e}")
        session.rollback()
    finally:
        session.close()