#  Encapsulation Practice Task: Bank Account Simulator
# 👉 Problem Statement:

# Create a class called BankAccount with the following features:

# 🔐 Requirements:
# 🔒 Private Variables:
# __account_holder (string)

# __balance (float)

# ✅ Public Methods:
# __init__(self, name, initial_balance) – initialize account holder and balance

# deposit(self, amount) – adds money to balance (only if amount > 0)

# withdraw(self, amount) – subtracts from balance (only if balance is enough)

# check_balance(self) – prints the current balance

# change_name(self, new_name) – updates the account holder name

# show_details(self) – prints name and current balance

class BankAccount:
    def __init__(self,name,initial_balance):
        self.__account_holder = name
        self.__balance = initial_balance


    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} is deposited")
    
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} is withdrawn")
        else:
            print("insuufcient balance")

    def check_balance(self):
        print(f"current balance:{self.__balance}")
    
    def change_name(self,new_name):
        self.__account_holder = new_name
        print(f"name changed to {new_name}")
    
    def show_details(self):
        print(f"name:{self.__account_holder} CB:{self.__balance}")
        

        
        






acc = BankAccount("Sanjay", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.check_balance()         # Output: ₹1300
acc.change_name("Rohit Sanjeev")
acc.show_details()          # Output: Account Holder: Rohit Sanjeev | Balance: ₹1300

