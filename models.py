from sqlalchemy import create_engine, String, Boolean, DateTime, ForeignKey, Numeric, Text, func, Enum as SQLEnum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from decimal import Decimal
from enum import Enum

class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///ledger.db")
Session = sessionmaker(bind=engine)


class TransactionType(Enum):
    deposit = "deposit"
    withdrawal = "withdrawal"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    wallet: Mapped["Account"] = relationship(
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )


class Account(Base):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )
    balance: Mapped[float] = mapped_column(default=0.0)

    user: Mapped["User"] = relationship(back_populates="wallet")



class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id"), nullable=False)
    type: Mapped[TransactionType] = mapped_column(
        SQLEnum(TransactionType), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    date: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    account: Mapped["Account"] = relationship(
        "Account", back_populates="transactions")
