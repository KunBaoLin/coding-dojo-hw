class User:
    def __init__(self,name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount
        return self
    
    def make_withdrawal(self,amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print (f"User:{self.name}, Blance:${self.amount}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self


leo = User('Leo')
joseph = User('Joseph')
frank = User('Frank')

leo.make_deposit(10000).make_deposit(1000).make_deposit(500).make_withdrawal(600).display_user_balance()

joseph.make_deposit(5000).make_deposit(6000).make_withdrawal(1100).make_withdrawal(100).display_user_balance()

frank.make_deposit(10000).make_withdrawal(500).make_withdrawal(200).make_withdrawal(300).display_user_balance().transfer_money(300,leo)
