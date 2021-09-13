class BankAccount:
    accounts = [] # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate # your code here! (remember, instance attributes go here)
        self.balance = balance 
        BankAccount.accounts.append(self)# don't worry about user info here; we'll involve the User class soon
    
    def deposit(self, amount):
        self.balance += amount
        return self # your code here
    
    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self # your code here
    
    def display_account_info(self):
        return(f"{self.balance}")  # your code here
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self # your code here

    @classmethod
    def print_all_infor(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:
    def __init__(self, name):
        self.name = name
        self.accounts = {
            "checking" : BankAccount(0.05,5000),
            "saving" : BankAccount(0.08,5000)
        }
    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.accounts['checking'].display_account_info()}")
        print(f"User: {self.name}, Saving Balance: {self.accounts['saving'].display_account_info()}")
        return self
    
    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

leo = User("Leo")
leo.accounts["checking"].deposit(2000)
leo.display_user_balance()
leo.accounts['saving'].deposit(1000)
leo.display_user_balance
