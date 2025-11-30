## 🏦 Bank Management System (Python CLI + Streamlit Web App)

A complete Bank Management System built using Python.
This project includes two fully functional versions:

✔ Command-Line Interface (CLI) — bank_project.py

✔ Streamlit Web App — app.py

Both versions allow users to create accounts, deposit and withdraw money, update details, and delete accounts — with all data stored safely in a JSON database.


---

## 🌐 Live Web App

👉 [Here's the link to use](https://bankmanagementproject-brt9pt282uavy8ddzzy7ql.streamlit.app/)


---

## 📌 Project Overview

This system simulates essential banking operations such as:

Creating a bank account

Depositing money

Withdrawing money

Viewing account details

Updating personal details

Deleting bank accounts


It uses a JSON file (data.json) for data persistence, making it lightweight and easy to run anywhere.


---

🖥️ 1. CLI Version (bank_project.py)

A menu-driven terminal interface that provides all banking features using user input.

CLI Features

Create new bank accounts

Auto-generate unique account numbers

Login using Account Number + PIN

Deposit money (limits included)

Withdraw money with balance check

Update name, email, or PIN

Delete accounts with confirmation

JSON-based data storage



---

🌐 2. Streamlit Web App (app.py)

A clean and modern web UI built using Streamlit.

Web App Features

Create bank accounts via form

Secure login system

Dashboard showing balance

Deposit / Withdraw money

Update user details instantly

Delete account with warning

Smooth UI powered by st.session_state

Automatic database updates

User-friendly error handling



---

## 🧠 What I Learned

Implementing file-based databases using JSON

Using Pathlib for file handling

Applying OOP concepts in a real-world banking simulation

Validating user input (PIN, age, amounts)

Building full CRUD operations (Create/Read/Update/Delete)

Using Streamlit to convert CLI programs into modern GUIs

Managing UI state with st.session_state

Safe database read/write operations

Creating web dashboards, forms, and conditional menus



---

## 🛠️ Technologies Used

Python

Streamlit

JSON (for storage)

Pathlib

Random & String modules

Session State Management



---

## ▶️ How to Run the Project


---

1️⃣ Run CLI Version

python bank_project.py

You will see options:

Create Account

Deposit

Withdraw

Show Details

Update Details

Delete Account

Quit



---

2️⃣ Run Streamlit Web App

Install Streamlit:

pip install streamlit

Run:

streamlit run app.py

Your browser will open automatically.


---

## 📜 Account Number Generation

Account numbers are generated using:

6 random letters

3 digits

2 special characters

All shuffled and combined


Example:

AjK$92xP1@


---
