'''
Create a class that represents a BankAccount.  Give each object a name and a balance.  Add a method to 
getDetails of these attributes.

Create a few BankAccount objects.

Add a class attribute (list) to keep track of the list of BankAccount objects.

Write a loop to print out the details of every BankAccount object
'''
class BankAccount: 
    store = []
    def __init__(self, name: str, balance: float):
        self.name = name 
        self.balance = balance 
        BankAccount.store.append(self.get_deets())

    def get_deets(self):
        return f"{self.name}: £{self.balance}"
    
    def print_objects(self): 
        for deet in BankAccount.store: 
            print(deet)

alice = BankAccount("Alice", 200.84)
bob = BankAccount("Bob", 100.50)

for account in BankAccount.store:
    print(account)
        
    