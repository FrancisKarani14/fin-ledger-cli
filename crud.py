from models import Account, Transaction, Session, TransactionType
from decimal import Decimal


def deposit(account_id, amount, description=""):
    session = Session()
    try:
        account = session.get(Account, account_id)
        if not account:
            raise ValueError("Account not found")

        txn = Transaction(
            account_id=account_id,
            type=TransactionType.deposit,
            amount=Decimal(amount),
            description=description,
        )

        account.balance += Decimal(amount)

        session.add(txn)
        session.commit()
        print("Deposit successful")
    finally:
        session.close()


def withdraw(account_id, amount, description=""):
    session = Session()
    try:
        account = session.get(Account, account_id)
        if not account:
            raise ValueError("Account not found")

        if account.balance < Decimal(amount):
            raise ValueError("Insufficient balance")

        txn = Transaction(
            account_id=account_id,
            type=TransactionType.withdrawal,
            amount=Decimal(amount),
            description=description,
        )

        account.balance -= Decimal(amount)

        session.add(txn)
        session.commit()
        print("Withdrawal successful")
    finally:
        session.close()
