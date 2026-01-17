from passlib.hash import bcrypt
from database import SessionLocal
from models import User

current_user = None


def signup(username, email, password, is_admin=False):
    db = SessionLocal()
    try:
        password_hash = bcrypt.hash(password)

        user = User(
            username=username,
            email=email,
            password=password_hash,
            is_admin=is_admin
        )

        db.add(user)
        db.commit()
        db.refresh(user)
        return user
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
