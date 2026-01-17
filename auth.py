from passlib.hash import bcrypt
from database import SessionLocal
from models import User, Account

current_user = None


def signup(username, email, password):
    db = SessionLocal()
    try:
        password_hash = bcrypt.hash(password)

        new_user = User(
            username=username,
            email=email,
            password=password_hash,
            
        )

        # auto create an account
        new_account = Account(balance=0.0)
        new_user.account = new_account

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    finally:
        db.close()


def login(username, password):
    global current_user
    db = SessionLocal()

    try:
        user = db.query(User).filter(User.username == username).first()
        if not user or not bcrypt.verify(password, user.password):
            return False

        current_user = user
        return True
    finally:
        db.close()


def require_login():
    if current_user is None:
        raise Exception("You must be logged in")
