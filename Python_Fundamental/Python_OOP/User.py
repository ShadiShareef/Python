class User:
    def __init__(self,name):
        self.name=name
        self.balance=0

    def make_withdrawal(self, amount):
        self.balance -=amount

    def make_deposits(self, amount):
        self.balance +=amount

    def display_user_balance(self):
        print(self.name +" balance = " , self.balance)
    
    def transfer_money(self,user1,amount):
        self.balance -=amount
        user1.balance +=amount

Shadi= User("Shadi Shareef")
Osama= User("Osama Shareef")
Anas= User("Anas Shareef")

Shadi.make_deposits(200)
Shadi.make_deposits(300)
Shadi.make_deposits(500)
Shadi.make_withdrawal(800)
Shadi.display_user_balance()

Osama.make_deposits(1000)
Osama.make_deposits(2500)
Osama.make_withdrawal(700)
Osama.make_withdrawal(800)
Osama.display_user_balance()

Anas.make_deposits(5000)
Anas.make_withdrawal(700)
Anas.make_withdrawal(800)
Anas.make_withdrawal(600)
Anas.display_user_balance()


Anas.transfer_money(Shadi,500)
Anas.display_user_balance()
Shadi.display_user_balance()