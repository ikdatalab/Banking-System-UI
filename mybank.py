import random

def open_account(accounts_list, cnic, account_title, initial_deposit):
    """Opens a new bank account and appends it to the session state list."""
    account = {
        'cnic': cnic,
        'title': account_title,
        'balance': initial_deposit,
        'account_number': random.randint(1000, 9999),
        'pin': random.randint(1000, 9999)
    }
    accounts_list.append(account)
    return account

def show_balance(accounts_list, account_number, pin):
    """Checks and returns the account balance securely."""
    for acc in accounts_list:
        if acc['account_number'] == account_number:
            if acc['pin'] == pin:
                return acc['balance'], None
            else:
                return None, "Invalid PIN"
    return None, "Account Not Found"

def deposit_amt(accounts_list, account_number, amount):
    """Deposits amount into the specified account."""
    for acc in accounts_list:
        if acc['account_number'] == account_number:
            acc['balance'] += amount
            return acc['balance'], None
    return None, "Account Not Found"

def withdraw_amt(accounts_list, account_number, pin, amount):
    """Withdraws amount if balance and PIN are valid."""
    for acc in accounts_list:
        if acc['account_number'] == account_number:
            if acc['pin'] != pin:
                return None, "Invalid PIN"
            if amount > acc['balance']:
                return None, "Insufficient Balance"
            acc['balance'] -= amount
            return acc['balance'], None
    return None, "Account Not Found"

def transfer_amt(accounts_list, account_number, pin, amount, beneficiary_acc):
    """Transfers amount between two accounts securely."""
    for acc in accounts_list:
        if acc['account_number'] == account_number:
            if acc['pin'] != pin:
                return None, "Invalid PIN"
            if acc['balance'] < amount:
                return None, "Insufficient Balance"
            
            # Check beneficiary
            for bacc in accounts_list:
                if bacc['account_number'] == beneficiary_acc:
                    acc['balance'] -= amount
                    bacc['balance'] += amount
                    return acc['balance'], None
            return None, "Beneficiary Account Not Found"
    return None, "Account Not Found"

def close_account(accounts_list, user_account, user_pin):
    """Closes account and returns remaining balance."""
    for i, acc in enumerate(accounts_list):
        if acc['account_number'] == user_account:
            if acc['pin'] == user_pin:
                remaining_amount = acc['balance']
                del accounts_list[i]
                return remaining_amount, None
            else:
                return None, "Invalid PIN"
    return None, "Account Not Found"