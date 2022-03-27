class BankAccount:
    def __init__(self, int_rate, balance):
        self.rate = int_rate			
        self.account_balance = balance
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self
    def display(self):
        print("Balance:",self.account_balance,"$","Rate: ",self.rate )
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self

class UserWithBank :
    def __init__(self, name, email_address,int_rate,balance):
        self.name = name		
        self.email = email_address	
        self.account = BankAccount(int_rate, balance)

user1=UserWithBank("Shadi","Shadi@gmail.com",0.5,200)
user1.account.make_deposit(300).make_deposit(100).make_deposit(200).make_withdrawal(100).display()
user2=UserWithBank("Anas","Anas@gmail.com",0.3,1000)
user2.account.make_deposit(100).make_deposit(200).make_withdrawal(50).make_withdrawal(100).make_withdrawal(150).make_withdrawal(200).display()