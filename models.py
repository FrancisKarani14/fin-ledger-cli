from sqlalchemy import Integer, Column, ForeignKey, Table, create_engine, Text, String, DateTime, Numeric
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Mapped, mapped_column
from decimal import Decimal

Base = declarative_base()
engine = create_engine('sqlite:///ledger.db')
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'
    #"""creates user tabe"""
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email:Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password_hash:Mapped[str] = mapped_column(String(255), nullable=False)
    is_admin:Mapped[bool] = mapped_column(default=False)
    accounts:Mapped[list["Account"]] = relationship("Account", back_populates="user")
   

class Account(Base):
    __tablename__ = 'accounts'
    #"""creates account table"""
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    account_name:Mapped[str] = mapped_column(String(100), nullable=False)
    balance:Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False, default=Decimal(0.00))

    user:Mapped["User"] = relationship("User", back_populates="accounts")

class Transaction(Base):
    __tablename__ = 'transactions'
    #"""creates transaction table"""
    id:Mapped[int] = mapped_column(primary_key=True)
    account_id:Mapped[int] = mapped_column(ForeignKey('accounts.id'), nullable=False)
    amount:Mapped[float] = mapped_column(nullable=False)
    description:Mapped[str] = mapped_column(Text)
    date:Mapped[DateTime] = mapped_column(DateTime, nullable=False)

    account:Mapped["Account"] = relationship("Account", back_populates="transactions")
