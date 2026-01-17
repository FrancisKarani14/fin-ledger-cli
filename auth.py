from passlib.context import CryptContext
# from sqlalchemy.orm import Session

from models import User, Account, SessionLocal

# password hashing context (recommended way)
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

_current_user = None


# -----------------------
# helpers
# -----------------------
def hash_password(password: str) -> str:
    if len(password.encode("utf-8")) > 72:
        raise ValueError("Password too long (max 72 bytes)")
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


# -----------------------
# auth actions
# -----------------------
def signup(username: str, email: str, password: str):
    session = SessionLocal()

    try:
        # prevent duplicates
        if session.query(User).filter_by(username=username).first():
            raise ValueError("Username already exists")

        if session.query(User).filter_by(email=email).first():
            raise ValueError("Email already exists")

        password = hash_password(password)

        user = User(
            username=username,
            email=email,
            password=password,
        )

        # auto-create wallet (1–1 relationship)
        user.wallet = Account(balance=0.0)

        session.add(user)
        session.commit()
        session.refresh(user)

        print("Signup successful. You can now log in.")
        return user

    finally:
        session.close()


def login(username: str, password: str) -> bool:
    global _current_user
    session = SessionLocal()


    try:
        user = session.query(User).filter_by(username=username).first()

        if not user or not verify_password(password, user.password):
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
