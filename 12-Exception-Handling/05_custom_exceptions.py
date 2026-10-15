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
    
 