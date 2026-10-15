'''
A custom exception is a user defined exception class
that represents a specific error in an application.
'''
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter you age: "))
    
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")
    
    print("Your age is:", age)
    
except InvalidAgeError as error:
    print("Age error:", error)
    
except ValueError:
    print("Please enter a valid integer.")
    
 # bank account
class InsufficientBalanceError(Exception):
     pass

balance = 40000

try:
    amount = float(input("Enter withdrawal amount: "))
    
    if amount < 0:
        raise ValueError("Amount must be positive")
    
    if amount > balance:
        raise InsufficientBalanceError(
            "You do not have enough balance in your account."
        )
    
    balance -= amount
    
    print("Withdrawal successful")
    print("Remaining balance:", balance)
    
except InsufficientBalanceError as error:
    print("Transaction failed.", error)
    
except ValueError as error:
    print("Invalid amount.", error)
    