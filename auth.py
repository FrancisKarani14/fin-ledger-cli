from passlib.hash import bcrypt
from models import User, Account, Session

_current_user = None


def signup(username, email, password):
    session = Session()
    try:
        password_hash = bcrypt.hash(password)

        user = User(
            username=username,
            email=email,
            password=password_hash,
        )

        # auto-create wallet (1–1 relationship)
        account = Account(balance=0.0)
        user.wallet = account

        session.add(user)
        session.commit()
        session.refresh(user)

        print("Signup successful. You can now log in.")
        return user
    finally:
        session.close()


def login(username, password):
    global _current_user
    session = Session()

    try:
        user = session.query(User).filter_by(username=username).first()

        if not user or not bcrypt.verify(password, user.password):
            print("Invalid username or password")
            return False

        _current_user = user
        print(f"Welcome, {user.username}")
        return True
    finally:
        session.close()


def logout():
    global _current_user
    _current_user = None
    print("Logged out successfully")


def get_current_user():
    return _current_user


def require_login():
    if _current_user is None:
        raise PermissionError("You must be logged in to perform this action")
