class BankAccount:
    def __init__(self,balance = 0): 
        self.int_rate=0.01
        self.balance = balance

    def deposit(self, amount):
        self.balance +=amount
        return self

    def withdraw(self, amount):
        self.balance -=amount
        if self.balance<0 :
            print("Insufficient funds: Charging a $5 fee")
            self.balance -=5
        return self
    def display_account_info(self):
        print("Account", self.balance," ,Interest:",self.int_rate)

    def yield_interest(self):
        if self.balance>0:
            self.balance+=self.balance*self.int_rate
        else :
            print("no yield interest the balance is negative")
        return self

rahaf_account= BankAccount(50)
rahaf_account.deposit(1500).deposit(700).deposit(600).withdraw(200).yield_interest().display_account_info()
shady_account= BankAccount(2000)
shady_account.deposit(3000).deposit(300).withdraw(1200).withdraw(600).withdraw(2000).withdraw(2000).yield_interest().display_account_info()
