# 🏦 Simple Banking System - Streamlit Web UI

A modular Python web application built using **Streamlit** that simulates core banking functions including account creation, balance checking, deposits, withdrawals, fund transfers, and account closure.

---

## 🚀 Features

- **Open Account:** Automatically generates a unique 4-digit Account Number and secure PIN.
- **Check Balance:** Verifies credentials and displays current balance.
- **Deposit Funds:** Instantly updates account balance.
- **Withdraw Funds:** Validates PIN and ensures balance sufficiency before processing.
- **Fund Transfer:** Transfer funds securely between two registered accounts.
- **Close Account:** Safely deletes account data and returns remaining cash balance.
- **Debug View:** Displays current active `st.session_state` JSON data.

---

## 🛠️ Project Structure

```text
├── mybank.py          # Core banking logic & error handling functions
├── app.py             # Streamlit user interface & state management
└── README.md          # Project documentation