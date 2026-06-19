#here we will build bank account class

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
        
    def deposite(self, amount):
        
        if amount< 5:
            raise ValueError("Deposite money should be at list $5")
        self._balance += amount
        return self._balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be in positive")
        if amount > self._balance:
            raise ValueError("INSUFFICIANT fund")
        
        self._balance -= amount
        return self._balance
    
    def get_balance(self):
        return self._balance
    
    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self._balance})"
    
    def __repr__(self):
        return f"BankAccount(owner='{self.owner}',balance ={self._balance})"
    
account = BankAccount("Arjun", 1000)
print(account)
account.deposite(1000)
print(account.get_balance())
account.withdraw(500)
print(account.get_balance())

try:
    account.withdraw(9999)
except ValueError as e:
    print(f"Error:{e}")         