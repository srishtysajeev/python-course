'''
1. Create the BankAccount class with deposit(), withdraw(), display().  Create 3 sample objects and
then call deposit(), withdraw() followed by display() for some of the objects.

2. Create a class attribute: accountsList and a method printAllAccounts()

3. Add an overdraft attribute to the BankAccount class and modify your code to generate exceptions
when the overdraft is exceeded
'''

class Overdrawn(Exception): pass
class UnknownAccount(Exception): pass
class InvalidAmount(Exception): pass

class BankAccount: 
    store = []
    def __init__(self, name: str, balance: float):
        self.name = name 
        self.balance = balance 
        BankAccount.store.append(self.get_deets())

    def get_deets(self):
        return f"{self.name}: £{self.balance}"
    
    def deposit(self, amount ):
        self.balance += amount 
         
    
    def withdraw(self, amount): 
        if amount + self.overdraft > self.balance: 
            print("Cannot withdraw money")
            raise ValueError 
        else: 
            self.balance -= amount 

    def overdraft(self, overdraft): 
        return overdraft

            


alice = BankAccount("Alice", 200.84)
bob = BankAccount("Bob", 100.50)

for account in BankAccount.store:
    print(account)
        