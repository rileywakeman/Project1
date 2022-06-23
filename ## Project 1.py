## Project 1

"""
Revature Big Data Next Gen Python / Scala Foundation Project Guidelines.

Project:
Create a Python application that connects to either a MySQL or MongoDB server,
and performs CRUD operations on a database.
    - The application must be able to create, read, update, and delete.
    - Use at least 3 different tables.
    - The tables must contain at minimum 50 records each.
    - The tables must have a primary / foreign key relationship.

Examples:
    A banking application
    Store transaction history
    A video game
    Insurance company records

Presentation:
    We will present our projects the morning of June 24th.
    Short 5 - 10 minute demonstration of all the functionalities of your project.

Other things of note:
    This is an individual assignment, no groups.
    You will be expected to back up your project using GitHub in case of any system crashes or data loss.
"""
##from multiprocessing.spawn import old_main_modules
##from turtle import update
import pymongo
import pprint
from pymongo import MongoClient, mongo_client

connection_url = MongoClient('localhost', 27017)

mydb = connection_url.BankingApplication
accountcol =  mydb["Banking"]
balance = mydb["Balance"]
history1 = mydb["Transactions"]

##Account Balance Collection
##Name :
##Account :
##Balance :

##Transaction Collection
##Name:
##Account:
##Type of Transaction:
##Amount :

## 1. create account
def create_account():
    print("To make an account please fill out the following, you cannot stop once you have started.")
    print("First and Last name")
    name1 = input("What is your full name? ")
    gender1 = input("What is your gender? ")
    print("Month/day/year, 00/00/0000")
    birthday1 = input("What is your date of birth? ")
    print("Ex. 000 lee roy Avenue(Street), California(State), 55555(Zip).")
    address1 = input("What is your address?  ")
    print("Ex. 000-000-0000")
    mobile1 = input("What is your mobile phone number? ")
    print("You can choose saving, checking, money market, and retirement.")
    account1 = input("What accounts would you like to open? ")
    """
    if account1 == "saving" | "Saving" | "savings" | "Savings":
        print("A saving account added")
    elif account1 == "checking" | "Checking":
        print("A Checking account added")
    elif account1 == "money market" | "Money Market":
        print("Money market account added")
    elif account1 == "retirement" | "Retirement":
        print("Retirement account")
    else: 
        print("Wrong input")
    """
    newaccount = {"name" : (name1), "Gender" : (gender1), "Birthday" : (birthday1), "address" : (address1), "Mobile" : (mobile1), "account" : (account1)}
    accountcol.insert_one(newaccount)

## 2. update account
def update_account():
    while True:
        print("what would you like to update? ")
        print("\t1. Name.")
        print("\t2. Address.")
        print("\t3. Mobile.")
        print("\t4. Account.")
        print("\t5. Back to Menu.")
        upsel = int(input("\nSelection: "))
        if upsel == 1:
            oldname = input("What is the existing name? ")
            newname = input("What is the new name? ")
            accountcol.update_one({"name" : oldname}, {"$set":{"name" : newname}})
        elif upsel == 2:
            oldaddress = input("what is the existing address? ")
            newaddress = input("What is the new address? ")
            accountcol.update_one({"address" : oldaddress}, {"$set":{"address" : newaddress}})
        elif upsel == 3:
            oldmobile = input("What si the existing mobile number? ")
            newmobile = input("What is the new number? ")
            accountcol.update_one({"Mobile" : oldmobile}, {"$set" :{"Mobile" : newmobile}})
        elif upsel == 4:
            oldaccount = input("What acount would you like to change? ")
            newaccount = input("What new account do you want to add or change? ")
            accountcol.update_one({"account" : oldaccount}, {"$set" :{"account" : newaccount}})
        elif upsel == 5:
            print("No more updates")
            print("Back to Menu")
            break

        else:
            print("wrong slection, please try again.")


## 3 delete account
def delete_account():
    print("Are you sure all you want to delete you account. ")
    print("You don't have to do this.")
    delete1 = input("Name of the account?")
    accountcol.delete_one({"name" : delete1})
    print("I can't belive you've done this!")

## 4.Check account balance
def account_balance():
    while True:
        print("\t1. New Search.")
        print("\t2. Back to Menu.")
        sel1 = int(input("\nSelect option "))
        if sel1 == 1:
            balance1()
        elif sel1 == 2: 
            print("Back to menu")
            break
        else:
            print("Wrong selection, please try again")
def balance1():
    findaccount = input("Please enter you name. ")
    y = balance.find({"name" : findaccount})
    for a in y: 
        print(a)

## 5. check transactions
def check_transaction():
    while True:
        print("\t1. New Search.")
        print("\t2. Back to Menu.")
        sel2 = int(input("\nSelect option "))
        if sel2 == 1:
            transaction()
        elif sel2 == 2: 
            print("Back to menu")
            break
        else:
            print("Wrong selection, please try again")
def transaction():
    hist = input("Please enter your full name? ")
    x = history1.find({"Name" : hist})
    for i in x:
        print(i)



def menu():
    while True:
        print("Welcome to Banking online!")
        print("What would you like to do?")
        print("\t1. Create a new account.")
        print("\t2. update an existing account.")
        print("\t3. Delete an existing account")
        print("\t4. check account balance.")
        print("\t5. check transaction.")
        print("\t6. Leave the application.")
        selection = int(input("\nSelection: "))
        if selection == 1:
            create_account()
        elif selection == 2:
            update_account()
        elif selection == 3:
            delete_account()
        elif selection == 4:
            account_balance()
        elif selection == 5:
            check_transaction()
        elif selection == 6:
            print("Thank you for visiting banking online!")
            break

        else:
            print("wrong slection, please try again.")
menu()
