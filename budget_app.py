import json

database = { }

class Budget():    

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
        
    def deposit(amount, bal):
        bal += amount
        return bal

    def withdraw(option, amount, bal):
        bal -= amount
        return bal 

    def transfer(db, option1, amount1, option2):
        db[option1] -= amount1
        db[option2] += amount1
        return db
    
    def balance(db):
        for categ, bal in db.items():
            print(categ, bal)

def init():
    print("Welcome to your budget app, proceed by selecting below options by their index/number")

    choice()

def choice():
    try:

        feedback = int(input("1) create a budget, 2) see all budget balance, 3) withdraw from a budget, 4) deposit to a budget, 5) transfer b/w budgets  6) quit \n"))
    except:
        print("Invalid input")
        choice()

    if feedback == 1:
        new_budget()
    elif feedback == 2:
        see_budgets()
    elif feedback == 3:
        debit()
    elif feedback == 4:
        credit()
    elif feedback == 5:
        transfers()
    elif feedback == 6:
        print("We hope you had a good budgeting experience, bye for now.")
        quit()
    else:
        print("Invalid opton selected")
        choice()


def new_budget():
    print("*** New Budget***")
    
    budget_title = input("Enter budget title \n")
    amount = int(input("Enter budget amount \n"))

    budget = Budget(budget_title, amount)
    database[budget_title] = amount
    print(" \n")
    print(f"Budget {budget_title} created with balance of {amount}")
    print(" \n")
    choice()


def see_budgets():
    print("*** See Budget ***")
    if len(database) == 0:
        print("You have not created a budget category")
        choice()
        print(" \n")
    else:
        count = 0
        for budget, balance in database.items():
            count += 1
            print(f" {count} {budget}  -  {balance} ")
        
        print(" \n")
        choice()

def debit():
    print("*** Withdraw ***")

    for key, value in database.items():
        print(f"-  {key}")

    option = input("Select a budget \n")
    if option in database:
        amt = int(input("Enter amount \n"))
        if amt < database[option]:
            balance = int(database[option])
        
            new_balance = Budget.withdraw(option, amt, balance)
        
            database[option] = new_balance
    else:
        print("You don't have this budget")
        debit()

    print("Current budgets after withdawal")
    for key, value in database.items():
        print(f"-  {key}, {value}")
    
    choice()

def credit():
    print("*** Deposit ***")

    for key, value in database.items():
        print(f"-  {key}")

    option = input("Select a budget \n")
    
    if option in database:
        amt = int(input("Enter amount \n"))
        
        balance = int(database[option])
    
        new_balance = Budget.deposit(amt, balance)
    
        database[option] = new_balance
    else:
        print("Something went wrong try again")
        credit()

    print("Current budgets after deposit")
    for key, value in database.items():
        print(f"-  {key}, {value}")
    
    choice()

def balance():
    print("*** Getting Balance***")
    check_bal = Budget.balance(database)
    if len(check_bal) == 0:
        print("You have no budget yet")
        choice()
    else:
        print(check_bal)

def transfers():
    print("** Transfer Operations, please enter required details for successful transfer")
    for key, value in database.items():
        print(key)
    try:

        from_budget = input("Enter buget your are transfering from \n")
        from_amount = int(input("Enter amount you want to transfer \n"))
        for key, value in database.items():
            print(key)
        to_budget = input("Enter destination of funds \n")
        print("\n")
    except:
        print("Invalid input, restart")
        transfers()

    db = Budget.transfer(database, from_budget, from_amount, to_budget)
    print("\n")
    print(f"You transfered {from_amount} from {from_budget} to {to_budget} ")
    for key, value in db.items():
        print(key, value)
    
    choice()


init()