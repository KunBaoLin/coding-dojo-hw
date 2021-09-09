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
        print(f"Balance: {self.balance}") 
        return self # your code here
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self # your code here

    @classmethod
    def print_all_infor(cls):
        for account in cls.accounts:
            account.display_account_info()


checking = BankAccount(0.05,5000)
saving = BankAccount(0.08,5000)

checking.deposit(500).deposit(500).deposit(500).withdraw(600).yield_interest().display_account_info()
saving.deposit(500).deposit(500).withdraw(200).withdraw(300).withdraw(200).withdraw(300).yield_interest().display_account_info()

BankAccount.print_all_infor()