from sqlalchemy import Integer, Column, ForeignKey, Table, create_engine, Text, String, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Mapped, mapped_column

Base = declarative_base()
engine = create_engine('sqlite:///ledger.db')
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'
    #"""creates user tabe"""
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email:Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    pasword:Mapped[int] = mapped_column(Integer(8), nullable=False)


class Account(Base):
    __tablename__ = 'accounts'
    #"""creates account table"""
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    account_name:Mapped[str] = mapped_column(String(100), nullable=False)
    balance:Mapped[float] = mapped_column(nullable=False, default=0.0)

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
