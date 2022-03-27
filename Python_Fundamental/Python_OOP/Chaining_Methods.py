class User:
    def __init__(self,name):
        self.name=name
        self.balance=0

    def make_withdrawal(self, amount):
        self.balance -=amount
        return self

    def make_deposits(self, amount):
        self.balance +=amount
        return self

    def display_user_balance(self):
        print(self.name +" balance = " , self.balance)
    
    def transfer_money(self,user1,amount):
        self.balance -=amount
        user1.balance +=amount

Shadi= User("Shadi Shareef")
Osama= User("Osama Shareef")
Anas= User("Anas Shareef")

Shadi.make_deposits(200).make_deposits(300).make_deposits(500).make_withdrawal(800).display_user_balance()
Osama.make_deposits(1000).make_deposits(2500).make_withdrawal(700).make_withdrawal(800).display_user_balance()
Anas.make_deposits(5000).make_withdrawal(700).make_withdrawal(800).make_withdrawal(600).display_user_balance()

Anas.transfer_money(Shadi,500)
Anas.display_user_balance()
Shadi.display_user_balance()