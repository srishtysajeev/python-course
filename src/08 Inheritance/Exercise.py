'''
Create a base class that represents a bank account.  Add methods to allow a customer to deposit() and withdraw() 
money and provide a method display_balance().

Then add two derived classes: SavingsAccount and CheckingAccount
In the SavingsAccount provide a method 
    apply_interest()

In the CheckingAccount provide
    order_statement()

Then test you code with the following code:
    if __name__ == "__main__":
        savings = SavingsAccount("Alice", 1000, 0.05)
        savings.display_balance()
        savings.withdraw(200)
        savings.apply_interest()

        checking = CheckingAccount("Bob", 500, 200)
        checking.display_balance()
        checking.withdraw(600)
        checking.withdraw(200)
        checking.order_statement()
'''

class Overdrawn(Exception): pass
class UnknownAccount(Exception): pass
class InvalidAmount(Exception): pass

class BankAccount:
    accounts = {}
    def transfer(*, toAccountName, fromAccountName, value):
        toAccount = BankAccount.getAccount(toAccountName)
        fromAccount = BankAccount.getAccount(fromAccountName)
        fromAccount.balance -= value
        if fromAccount.isOverdrawn():
            fromAccount.balance += value
            fromAccount.withdraw(value)      # just to generate error message
        else:
            toAccount.balance += value

    def __init__(self, name, openingBalance, overdraftLimit=-1000):
        self.name = name
        self.balance = openingBalance
        self.overdraftLimit = overdraftLimit
        BankAccount.accounts[name] = self

    def isOverdrawn(self):
        return self.balance < self.overdraftLimit
    
    def deposit(self, value):
        if value < 0: raise InvalidAmount()
        self.balance += value

    def withdraw(self, value):
        balance = self.balance          # take a snapshot in case we need to roll back
        try:
            self.balance -= value
            if self.balance < self.overdraftLimit:
                raise Overdrawn()
        except Overdrawn as e:
            errorMessage = (f"{self.name}: can't withdraw {value} - would go overdrawn," 
                            f" current balance = {balance} and overdraft limit is {self.overdraftLimit}")
            print(errorMessage)
            self.balance = balance
            
    def printAllAccounts():
        for name,account in BankAccount.accounts.items():
            print(f"{name}: balance = {account.balance}")

    def getAccount(name):
        return BankAccount.accounts[name]
    

class SavingsAccount(BankAccount):