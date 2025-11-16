import streamlit as st
import json
import random
import string
from pathlib import Path

# ============================================================
#   BANK CLASS — SAME LOGIC, BUT STREAMLIT FRIENDLY
# ============================================================

class Bank:
    database = "data.json"
    data = []

    # Load database on start
    try:
        if Path(database).exists():
            with open(database) as f:
                data = json.load(f)
        else:
            with open(database, "w") as f:
                f.write("[]")
    except Exception as e:
        st.error(f"Error loading database: {e}")

    @classmethod
    def save(cls):
        with open(cls.database, "w") as f:
            json.dump(cls.data, f, indent=4)

    @classmethod
    def generate_acc_no(cls):
        alpha = random.choices(string.ascii_letters, k=6)
        num = random.choices(string.digits, k=3)
        spchr = random.choices("$@!$#%&", k=2)
        acc = alpha + num + spchr
        random.shuffle(acc)
        return "".join(acc)

    @classmethod
    def create_account(cls, name, age, email, pin):
        if age < 18:
            return False, "Age must be 18 or above."

        if len(str(pin)) != 4:
            return False, "PIN must be 4 digits."

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountno": cls.generate_acc_no(),
            "balance": 0,
        }

        cls.data.append(info)
        cls.save()
        return True, info

    @classmethod
    def login(cls, accno, pin):
        for u in cls.data:
            if u["accountno"] == accno and u["pin"] == pin:
                return True, u
        return False, None

    @classmethod
    def deposit(cls, user, amount):
        user["balance"] += amount
        cls.save()

    @classmethod
    def withdraw(cls, user, amount):
        if user["balance"] < amount:
            return False
        user["balance"] -= amount
        cls.save()
        return True

    @classmethod
    def update(cls, user, name, email, pin):
        if name:
            user["name"] = name
        if email:
            user["email"] = email
        if pin:
            if len(pin) != 4:
                return False, "PIN must be 4 digits."
            user["pin"] = pin
        cls.save()
        return True, "Updated successfully."

    @classmethod
    def delete(cls, user):
        acc = user["accountno"]
       # Keep only users whose account number does NOT match
        cls.data = [u for u in cls.data if u["accountno"] != acc]
        cls.save()



# ============================================================
#   STREAMLIT APP UI
# ============================================================

st.set_page_config(page_title="Bank Management", page_icon="🏦", layout="centered")

st.title("🏦 Bank Management System")
st.write("A simple banking system built with Python + Streamlit.")

menu = st.sidebar.radio("Menu", ["Create Account", "Login", "About"])

# ============================================================
#   CREATE ACCOUNT
# ============================================================

if menu == "Create Account":
    st.header("➕ Create New Bank Account")

    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", max_chars=4, type="password")

    if st.button("Create Account"):
        if not name or not email or not pin:
            st.error("All fields are required.")
        else:
            ok, result = Bank.create_account(name, age, email, pin)
            if ok:
                st.success("🎉 Account created successfully!")
                st.code(f"YOUR ACCOUNT NUMBER:\n{result['accountno']}")
            else:
                st.error(result)


# ============================================================
#   LOGIN SYSTEM
# ============================================================

elif menu == "Login":
    st.header("🔐 Login to Your Account")

    accno = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password", max_chars=4)

    if st.button("Login"):
        ok, user = Bank.login(accno, pin)
        if not ok:
            st.error("Invalid account number or PIN")
        else:
            st.session_state["user"] = user
            st.success("Logged in successfully!")

    # If logged in, display dashboard
    if "user" in st.session_state:
        user = st.session_state["user"]

        st.subheader(f"👋 Welcome, {user['name']}!")
        st.info(f"**Balance:** ${user['balance']}")

        choice = st.radio("Choose Action", ["Deposit", "Withdraw", "Update Info", "Delete Account"])

        # Deposit
        if choice == "Deposit":
            amount = st.number_input("Amount to Deposit", min_value=1)
            if st.button("Deposit Money"):
                if amount > 15000:
                    st.error("Max deposit per transaction: 15000")
                else:
                    Bank.deposit(user, amount)
                    st.success(f"Deposited ${amount} successfully.")
                    st.rerun()

        # Withdraw
        if choice == "Withdraw":
            amount = st.number_input("Amount to Withdraw", min_value=1)
            if st.button("Withdraw Money"):
                ok = Bank.withdraw(user, amount)
                if ok:
                    st.success(f"Withdrew ${amount} successfully.")
                    st.rerun()
                else:
                    st.error("Insufficient balance.")

        # Update info
        if choice == "Update Info":
            new_name = st.text_input("New Name (optional)")
            new_email = st.text_input("New Email (optional)")
            new_pin = st.text_input("New PIN (optional)", max_chars=4)

            if st.button("Update Details"):
                ok, msg = Bank.update(user, new_name, new_email, new_pin)
                if ok:
                    st.success(msg)
                    st.rerun()
                else:
                    st.error(msg)

        # Delete account
        if choice == "Delete Account":
            st.error("⚠ This will permanently delete your account.")
            confirm = st.checkbox("I understand, delete my account")
            if confirm and st.button("Delete My Account"):
                Bank.delete(user)
                st.session_state.pop("user")
                st.success("Account deleted successfully.")
                st.rerun()


# ============================================================
#   ABOUT SECTION
# ============================================================

else:
    st.header("ℹ About This App")
    st.write("""
    This Bank Management System was converted from a Python CLI program 
    into a full Streamlit web interface.
    
    Features:
    - Create account  
    - Deposit/Withdraw  
    - View & update details  
    - Delete account  
    - JSON database  
    """)

