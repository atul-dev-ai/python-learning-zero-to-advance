'''
- An exception is an event that interrupts tha normal flow of a program.
Exception handling allows us to repond to certain runtime errors instead 
of letting the program terminate unexpectedly.
'''

# Normal error:
a = 10
b = 0
# result = a / b
# print(result)

# try except
try:
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero.")

# try & except with user input
try:
    number = int(input("Enter a number: "))
    print("Your value is:", number)
except ValueError:
    print("Please enter a valid integer.")

# finally
try:
    print("Program is running.")
except Exception:
    print("Something went wrong")
finally:
    '''
    The finally block is commonly used for cleaup tasks that should run whether an
    exception occurs or not.
    '''
    print("Program is finished.")

