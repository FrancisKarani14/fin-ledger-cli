from decimal import Decimal
from models import SessionLocal, Transaction, TransactionType
from auth import require_login


def deposit(amount: Decimal, description: str = ""):
    user = require_login()
    db = SessionLocal()

    try:
        account = db.get(type(user.wallet), user.wallet.id)

        account.balance += amount

        tx = Transaction(
            account=account,
            type=TransactionType.deposit,
            amount=amount,
            description=description
        )

        db.add(tx)
        db.commit()
        print(f"Deposited {amount}. Balance: {account.balance}")
    finally:
        db.close()


def withdraw(amount: Decimal, description: str = ""):
    user = require_login()
    db = SessionLocal()

    try:
        account = db.get(type(user.wallet), user.wallet.id)

        if account.balance < amount:
            print("Insufficient funds")
            return

        account.balance -= amount

        tx = Transaction(
            account=account,
            type=TransactionType.withdrawal,
            amount=amount,
            description=description
        )

        db.add(tx)
        db.commit()
        print(f"Withdrew {amount}. Balance: {account.balance}")
    finally:
        db.close()
