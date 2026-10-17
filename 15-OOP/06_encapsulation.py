'''
Encapsulation combines data and related methods within a class and 
provides controlled ways to access or modify that data.
'''

# no validation
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

account = BankAccount(5000)

account.balance = -1000
print(account.balance)

# private attribute
class BankAccount:
    def __init__(self, balance):
        