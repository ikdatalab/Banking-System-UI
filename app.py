import streamlit as st
from mybank import (
    open_account, 
    show_balance, 
    deposit_amt, 
    withdraw_amt, 
    transfer_amt, 
    close_account
)

# ---------------------------------------------
# Initialize Session State
# ---------------------------------------------
if "all_accounts" not in st.session_state:
    st.session_state.all_accounts = []

st.title("🏦 Simple Banking System - Streamlit Interface")

menu = st.sidebar.selectbox(
    "Select Action",
    ["Open Account", "Check Balance", "Deposit", "Withdraw", "Transfer", "Close Account", "Show All Accounts"]
)

# ---------------------------------------------
# 1. Open Account
# ---------------------------------------------
if menu == "Open Account":
    st.header("➕ Open a New Account")

    cnic = st.text_input("Enter CNIC (without dashes)")
    title = st.text_input("Account Title")
    deposit = st.number_input("Initial Deposit", min_value=0, value=0)

    if st.button("Create Account"):
        if title.strip() == "":
            st.error("Please enter a valid account title.")
        else:
            acc = open_account(st.session_state.all_accounts, cnic, title, deposit)
            st.success("🎉 Account Created Successfully!")
            st.write(f"**Account Number:** `{acc['account_number']}`")
            st.write(f"**PIN:** `{acc['pin']}` *(Save this PIN safely!)*")

# ---------------------------------------------
# 2. Check Balance
# ---------------------------------------------
elif menu == "Check Balance":
    st.header("💰 Check Balance")

    acc_no = st.number_input("Account Number", min_value=1000, max_value=9999, step=1)
    pin = st.number_input("PIN", min_value=1000, max_value=9999, step=1, format="%d")

    if st.button("Show Balance"):
        bal, err = show_balance(st.session_state.all_accounts, acc_no, pin)
        if err:
            st.error(err)
        else:
            st.success(f"Your Current Balance is: **Rs {bal}**")

# ---------------------------------------------
# 3. Deposit
# ---------------------------------------------
elif menu == "Deposit":
    st.header("📥 Deposit Amount")

    acc_no = st.number_input("Account Number", min_value=1000, max_value=9999, step=1)
    amt = st.number_input("Amount to Deposit", min_value=1, value=500)

    if st.button("Deposit"):
        bal, err = deposit_amt(st.session_state.all_accounts, acc_no, amt)
        if err:
            st.error(err)
        else:
            st.success(f"Amount Deposited Successfully! New Balance: **Rs {bal}**")

# ---------------------------------------------
# 4. Withdraw
# ---------------------------------------------
elif menu == "Withdraw":
    st.header("📤 Withdraw Amount")

    acc_no = st.number_input("Account Number", min_value=1000, max_value=9999, step=1)
    pin = st.number_input("PIN", min_value=1000, max_value=9999, step=1, format="%d")
    amt = st.number_input("Amount to Withdraw", min_value=1, value=500)

    if st.button("Withdraw"):
        bal, err = withdraw_amt(st.session_state.all_accounts, acc_no, pin, amt)
        if err:
            st.error(err)
        else:
            st.success(f"Withdrawal Successful! New Balance: **Rs {bal}**")

# ---------------------------------------------
# 5. Transfer
# ---------------------------------------------
elif menu == "Transfer":
    st.header("💸 Transfer Amount")

    acc_no = st.number_input("Your Account Number", min_value=1000, max_value=9999, step=1)
    pin = st.number_input("Your PIN", min_value=1000, max_value=9999, step=1, format="%d")
    amt = st.number_input("Amount to Transfer", min_value=1, value=500)
    ben = st.number_input("Beneficiary Account Number", min_value=1000, max_value=9999, step=1)

    if st.button("Transfer"):
        bal, err = transfer_amt(st.session_state.all_accounts, acc_no, pin, amt, ben)
        if err:
            st.error(err)
        else:
            st.success(f"Transfer Successful! Remaining Balance: **Rs {bal}**")

# ---------------------------------------------
# 6. Close Account
# ---------------------------------------------
elif menu == "Close Account":
    st.header("❌ Close Account")

    acc_no = st.number_input("Account Number", min_value=1000, max_value=9999, step=1)
    pin = st.number_input("PIN", min_value=1000, max_value=9999, step=1, format="%d")

    if st.button("Close Account"):
        rem_amt, err = close_account(st.session_state.all_accounts, acc_no, pin)
        if err:
            st.error(err)
        else:
            st.success(f"Account closed successfully! Please collect your cash: **Rs {rem_amt}**")

# ---------------------------------------------
# 7. Show All Accounts (Debug View)
# ---------------------------------------------
elif menu == "Show All Accounts":
    st.header("📋 All Accounts (Debug View)")
    if st.session_state.all_accounts:
        st.write(st.session_state.all_accounts)
    else:
        st.info("No accounts created yet in session state.")