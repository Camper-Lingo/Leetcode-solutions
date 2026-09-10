'''
Bank Account Management System

Implement a simple banking system using object-oriented programming in Python.

The system should allow users to:

Create bank accounts with a unique ID and account holder.
Find accounts by their ID.
Deposit and withdraw money from an account.
Transfer money between two accounts.
Prevent invalid transactions and transfers when the source account has insufficient funds.

Use separate Account and Bank classes, with the Bank class responsible for managing multiple Account objects.
'''
class Account:
    def __init__(self, id: int, holder: str):
        self.id = id
        self.holder = holder
        self.balance = 0.0

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount

    def withdraw(self,amount: float) -> bool:
        if amount> 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False

class Bank:
    def __init__(self):
        self.accounts = {}
    def create_account(self, id: int, holder: str) -> None:
        if id not in self.accounts:
            account = Account(id,holder)
            self.accounts[id] = account
        else:
            print("ID already in use!")

    def find_account(self, id: int) -> Account | None:
        if id in self.accounts:
            return self.accounts[id]
        return None

    def transfer(self, start_id: int, end_id: int, value: float) -> bool:
        start = self.find_account(start_id)
        end = self.find_account(end_id)
        if start is None or end is None:
            return False
        if value <= 0:
            return False
        if start.balance >= value:
            start.balance -= value
            end.balance += value
            return True
        return False
    
bank = Bank()

bank.create_account(1,"john")
bank.create_account(2,"thomas")
john = bank.find_account(1)
john.deposit(1000)
thomas =  bank.find_account(2)
thomas.deposit(1000)

bank.transfer(1,2,200)

print(thomas.balance,john.balance)




