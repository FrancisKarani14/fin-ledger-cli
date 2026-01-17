from passlib.hash import bcrypt
from models import SessionLocal, User, Account
from decimal import Decimal

current_user: User | None = None


def signup(username: str, email: str, password: str) -> User:
    db = SessionLocal()
    try:
        password_hash = bcrypt.hash(password)

        user = User(
            username=username,
            email=email,
            password_hash=password_hash
        )

        # 🔐 Auto-create wallet
        wallet = Account(balance=Decimal("0.00"))
        user.wallet = wallet

        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    finally:
        db.close()


def login(username: str, password: str) -> bool:
    global current_user
    db = SessionLocal()

    try:
        user = db.query(User).filter_by(username=username).first()

        if not user or not bcrypt.verify(password, user.password_hash):
            return False

        current_user = user
        return True
    finally:
        db.close()


def require_login() -> User:
    if current_user is None:
        raise Exception("You must be logged in")
    return current_user
