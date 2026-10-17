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
        self.__balance = balance

    def show_balance (self):
        print("Balance:", self.__balance)

account = BankAccount(5000)
account.show_balance()

# balance change using method
class BankAcc:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive")
            return

        self.__balance += amount
        print("Deposite successful")

    def withdrawal(self, amount):
        if amount <= 0:
            print("Amount must be positive")

        elif amount > self.__balance:
            print("Insufficient balance")

        else:
            self.__balance -= amount
            print("Withdrawal successful")

account = BankAcc(5000)

account.deposit(2000)
account.withdrawal(1500)
account.show_balance()

