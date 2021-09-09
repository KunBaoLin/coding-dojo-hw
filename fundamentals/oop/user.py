class User:
    def __init__(self,name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount
    
    def make_withdrawal(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print (f"User:{self.name}, Blance:${self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()

leo = User('Leo')
joseph = User('Joseph')
frank = User('Frank')

leo.make_deposit(10000)
leo.make_deposit(1000)
leo.make_deposit(500)
leo.make_withdrawal(600)
leo.display_user_balance()

joseph.make_deposit(5000)
joseph.make_deposit(6000)
joseph.make_withdrawal(1100)
joseph.make_withdrawal(100)
joseph.display_user_balance()

frank.make_deposit(10000)
frank.make_withdrawal(500)
frank.make_withdrawal(200)
frank.make_withdrawal(300)
frank.display_user_balance

frank.transfer_money(300,leo)