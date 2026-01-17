Here’s a **clean, professional, senior-level README** rewritten in proper Markdown. I’ve fixed grammar, structure, consistency, and added the missing but expected sections (overview, architecture, usage, security notes, roadmap).

You can copy-paste this directly into your `README.md`.

---

# 💰 Fin-Ledger-CLI

**Fin-Ledger-CLI** is a command-line financial ledger application written in **Python**.
It simulates basic banking operations, allowing **administrators** to manage users and accounts, and **users** to perform transactions such as deposits and withdrawals — all from the terminal.

This project is designed as a **backend-focused CLI system**, emphasizing clean architecture, data integrity, and auditability using SQLAlchemy and Alembic.

---

## ✨ Features

### 🔐 Authentication & Roles

* CLI-based login system
* Role-based access (Admin vs User)

### 👤 User & Account Management (Admin)

* Create users
* Create accounts
* Delete accounts

### 💸 Transactions (Users)

* Deposit funds
* Withdraw funds
* View account balance
* Transaction history (audit trail)

### 🧾 Data Integrity

* Transactions recorded immutably
* Account balances derived from transactional logic
* Database migrations with Alembic

---

## 🛠️ Technologies Used

* **Python 3.13.0**
* **Pipenv** – dependency & virtual environment management
* **SQLAlchemy (2.0 style)** – ORM and database modeling
* **Alembic** – database migrations
* **Click** – command-line interface framework
* **SQLite** – lightweight relational database (default)

---

## 📁 Project Structure

```
fin-ledger-cli/
├── alembic/              # Database migrations
├── alembic.ini
├── cli.py                # CLI entry point
├── models.py             # SQLAlchemy models
├── database.py           # Engine & session setup
├── crud.py               # Database operations
├── auth.py               # Authentication logic
└── README.md
```

---

## ⚙️ Setup & Installation

### Prerequisites

* Laptop or desktop computer
* Python 3.13+
* Git
* Pipenv
* VS Code (recommended)

---

### 🚀 Installation Steps

1. **Clone the repository**

   ```bash
   git clone git@github.com:FrancisKarani14/fin-ledger-cli.git
   cd fin-ledger-cli
   ```

2. **Install dependencies**

   ```bash
   pipenv install
   ```

3. **Activate virtual environment**

   ```bash
   pipenv shell
   ```

4. **Run database migrations**

   ```bash
   alembic upgrade head
   ```

5. **Start the CLI**

   ```bash
   python cli.py
   ```

---

## 🖥️ Usage

Once the CLI starts, you will be presented with an interactive menu similar to the example below:

<img width="341" height="192" alt="CLI Screenshot" src="https://github.com/user-attachments/assets/9ab967e1-9fc6-47dc-aadf-7abb89b63e50" />

Follow the on-screen prompts to:

* Log in
* Create users/accounts (admin)
* Deposit or withdraw funds
* View balances

---

## 🔐 Security Notes

* Passwords are **hashed** (never stored in plain text)
* All financial operations are **transaction-driven**
* Direct balance mutation is avoided to preserve auditability

> ⚠️ This project is for learning and demonstration purposes and should not be used as-is in production financial systems.

---

## 🧭 Roadmap (Future Improvements)

* Persistent CLI sessions (token-based auth)
* Account locking & overdraft rules
* Export transaction history (CSV / JSON)
* PostgreSQL support
* Automated tests (pytest)

---

## 👤 Author

**Francis Karani**
Software Engineer

* GitHub: [@FrancisKarani14](https://github.com/FrancisKarani14)

---

## 📄 License

MIT License

Copyright (c) 2026 Francis Karani

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND.

---


