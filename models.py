from sqlalchemy import (
    create_engine,
    String,
    DateTime,
    ForeignKey,
    Numeric,
    Text,
    func,
    Enum as SQLEnum,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from decimal import Decimal
from enum import Enum

# ---------------- Base ----------------


class Base(DeclarativeBase):
    pass


engine = create_engine("sqlite:///ledger.db", echo=False)
SessionLocal = sessionmaker(bind=engine)

# ---------------- Enums ----------------


class TransactionType(Enum):
    deposit = "deposit"
    withdrawal = "withdrawal"

# ---------------- Models ----------------


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    wallet: Mapped["Account"] = relationship(
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
        lazy="joined"
    )


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )
    balance: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        default=Decimal("0.00")
    )

    user: Mapped["User"] = relationship(back_populates="wallet")
    transactions: Mapped[list["Transaction"]] = relationship(
        back_populates="account",
        cascade="all, delete-orphan"
    )


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id"),
        nullable=False
    )
    type: Mapped[TransactionType] = mapped_column(
        SQLEnum(TransactionType),
        nullable=False
    )
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    date: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    account: Mapped["Account"] = relationship(back_populates="transactions")


def init_db():
    Base.metadata.create_all(engine)
