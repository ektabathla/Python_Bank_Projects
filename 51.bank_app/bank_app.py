"""
    Bank Application

        It Contains Functions like

            login, signup
            debit, credit, check-balance, logout
            main_menu, sub_menu
"""
from getpass import getpass
import os
import time
import json

def get_last_acc_number():
    with open("last_account.json", "r") as fp:
        acc = json.load(fp)
    return acc
def update_last_acc_number(acc):
    with open("last_account.json", "w") as fp:
        json.dump(acc, fp)
        
def create_new_account(record):
    old = get_last_acc_number()
    new = old+1
    update_last_acc_number(new)
    with open(f"accounts/{new}", "w") as fp:
        json.dump(record, fp)
    return new

def signup():
    """
        ask user for details and create a new account
    """
    name = input("name: ").strip().lower()
    balance = float(input("balance: "))
    password = getpass("Password: ")
    record = {
        "name": name,
        "balance": balance,
        "password": password,
    }

    new_acc =  create_new_account(record)
    
    print(f"New Account Created! note account number {new_acc}")

    
def login():
    """
        will try to logged in a user
    """
    global database
    acc = int(input("Account Number: "))
    if acc in database.keys():
        password = getpass("Password: ")
        db_password = database[acc]["password"]
        if password == db_password:
            name = database[acc]["name"]
            print(f"Welcome Back user! {name.title()}")
            return acc
        else:
            print("!Error!Invalid Password!")
            print("Please Try Again")
            return False
    else:
        print("!Error! Invalid Account Number!")
        print("Please Check Account Number and Try Again!")
        print("Or just create new account by signing up!")
        return False
        
def debit(acc, amount):
    """
        try deduct balance from user account
    """
    global database
    #amount = float(input("Amount to Debit: "))
    account_balance = database[acc]["balance"]
    if amount <= account_balance:
        database[acc]["balance"] -= amount
        print(f"!{amount}\u20B9!Sucessfully Debited from your account!")
        print(f"Your Remaining Balance is {database[acc]['balance']}\u20B9.")
    else:
        print("!Error! In-sufficient Account Balance.")
        print(f"You only have {account_balance}\u20B9 in your account.")


def credit(acc, amount):
    global database
    database[acc]['balance'] += amount
    print(f"!Your account sucessfully credited for {amount}\u20B9!")
    print(f"Your updated balance is {database[acc]['balance']}\u20B9!")
    
def check_balance(acc):
    """
        display balance of user account
    """
    global database
    bal = database[acc]["balance"]
    print(f"You have {bal}\u20B9 in your account.")

def main_menu():
    """
        Main Menu for Bank Application
    """
    menu = """
    1. Login
    2. Signup
    3. Exit
    """
    print(menu)
    ch = input("choice: ")
    if ch == "1":
        acc = login()
        if acc:
            sub_menu(acc)
    elif ch == "2":
        signup()
    
    elif ch == "3":
        print("\n\nThanks for using Our Services\n\n")
        print("..................bye bye.........")
        exit(0)
    else:
        print("!Invalid Choice Please Select 1, 2, or 3!")


def sub_menu(acc):
    """
        Sub Menu for bank application
    """
    
    menu = """
        1. Debit
        2. Credit
        3. Check Balance
        4. Logout
    """
    while True:
        print(menu)
        ch = input("Choice: ")
        if ch == "1":
            amount = float(input("Enter Amount: "))
            debit(acc, amount)
        elif ch == "2":
            amount = float(input("Enter Amount: "))
            credit(acc, amount)
        elif ch == "3":
            check_balance(acc)
        elif ch == "4":
            print("\n\nBye Bye See you Soon!\n")
            break
        else:
            print("\nInvalid Choice choose from 1, 2, 3 or 4")
            
if __name__ == "__main__":
    while True:
        os.system("cls")
        print("\n\n\n\n")
        print("Welcome to Python Bank".center(100))
        print("\n\n\n")
        main_menu()
        #time.sleep(10)
        input("\n\n\npress Enter to continue")
