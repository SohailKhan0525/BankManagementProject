# 🏦 Bank Management System (Python CLI + Streamlit Web App)

A complete Bank Management System built using Python.
This project includes two fully functional versions:

- ✔ **Command-Line Interface (CLI)** — `bank_project.py`
- ✔ **Streamlit Web App** — `app.py`

Both versions allow users to create accounts, deposit and withdraw money, update details, and delete accounts — with all data stored safely in a JSON database.

---

## 🌐 Live Web App

👉 [Here's the link to use](https://bankmanagementproject-brt9pt282uavy8ddzzy7ql.streamlit.app/)

---

## 📌 Project Overview

This system simulates essential banking operations such as:

- Creating a bank account
- Depositing money
- Withdrawing money
- Viewing account details
- Updating personal details
- Deleting bank accounts

It uses a JSON file (`data.json`) for data persistence, making it lightweight and easy to run anywhere.

---

## 🖥️ 1. CLI Version (`bank_project.py`)

A menu-driven terminal interface that provides all banking features using user input.

### CLI Features

- ✅ Create new bank accounts
- ✅ Auto-generate unique account numbers
- ✅ Login using Account Number + PIN
- ✅ Deposit money (limits included)
- ✅ Withdraw money with balance check
- ✅ Update name, email, or PIN
- ✅ Delete accounts with confirmation
- ✅ JSON-based data storage

---

## 🌐 2. Streamlit Web App (`app.py`)

A clean and modern web UI built using Streamlit.

### Web App Features

- ✅ Create bank accounts via form
- ✅ Secure login system
- ✅ Dashboard showing balance
- ✅ Deposit / Withdraw money
- ✅ Update user details instantly
- ✅ Delete account with warning
- ✅ Smooth UI powered by `st.session_state`
- ✅ Automatic database updates
- ✅ User-friendly error handling

---

## 🧠 What I Learned

### Object-Oriented Programming (OOP)
- Designing a `Bank` class with **class-level attributes** (`data`, `database`) shared across all instances
- Using **`@classmethod`** methods so operations work on the shared class state
- Implementing **private methods** (`__update`, `__generateaccountno`) to encapsulate internal logic and prevent outside access

### JSON File Handling (Data Persistence)
- Reading and writing a **JSON file** (`data.json`) as a lightweight database
- Using `json.loads()` / `json.dumps()` for serialisation
- Understanding why a file-based database is useful when a full SQL/NoSQL setup is not available

### Pathlib for File Operations
- Using `Path(filename).exists()` to **safely check** if a file exists before reading it
- Automatically creating the database file on first run if it is missing

### Input Validation
- Validating **age** (must be 18 or above) before creating an account
- Validating **PIN length** (must be exactly 4 digits)
- Validating **deposit limits** (amount must be between 0 and 15,000)
- Checking **sufficient balance** before allowing a withdrawal

### CRUD Operations
- **C**reate — collecting user details and appending a new record to the JSON list
- **R**ead — filtering the list with a **list comprehension** to find the matching account
- **U**pdate — selectively overwriting only the fields that changed, then saving back to disk
- **D**elete — removing the record by index and persisting the updated list

### Random & String Modules
- Generating **unique account numbers** by combining `random.choices()` on `string.ascii_letters`, `string.digits`, and special characters
- Using `random.shuffle()` to randomise the order so the format is unpredictable

### Error Handling
- Wrapping file I/O in `try/except` blocks to catch unexpected errors on startup
- Catching non-numeric input in the main menu loop with `try/except`

### Menu-Driven CLI Design
- Building an interactive `while True` loop that keeps running until the user presses **7 to quit**
- Mapping numeric choices to the appropriate method calls cleanly

### Streamlit Web Development
- Converting the CLI program into a **modern web app** using Streamlit
- Using `st.session_state` to persist the logged-in user across page interactions
- Building forms, radio buttons, number inputs, and conditional UI sections
- Calling `st.rerun()` to refresh the page after state-changing operations

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web app UI |
| JSON | Data storage |
| Pathlib | File path handling |
| `random` & `string` | Account number generation |
| `st.session_state` | Session / state management |

---

## ▶️ How to Run the Project

### 1️⃣ Run CLI Version

```bash
python bank_project.py
```

You will see the following menu:

```
Press '1' to create an account
Press '2' to deposit money
Press '3' to withdraw money
Press '4' to see the details
Press '5' to update the details
Press '6' to delete an account
Press '7' to quit
```

### 2️⃣ Run Streamlit Web App

Install Streamlit (if not already installed):

```bash
pip install streamlit
```

Run the app:

```bash
streamlit run app.py
```

Your browser will open automatically at `http://localhost:8501`.

---

## 📜 Account Number Generation

Account numbers are generated using:

- 6 random letters (`string.ascii_letters`)
- 3 random digits (`string.digits`)
- 2 random special characters (`$@!#%&`)
- All shuffled together using `random.shuffle()`

Example output:

```
AjK$92xP1@
```

---
