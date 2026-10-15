'''
The "else" block executes only when the "try" block
completes without raising an exception.
'''
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    result = num1 / num2
    
except ValueError:
    print("Please enter valid numbers.")
    
except ZeroDivisionError:
    print("Cannot divide by zero.")
    
else:
    print("Result:", result)
    print("Calculation Successful!")
    
'''
The "finally" block normally executes whether an exception
occurs or not, making it useful for cleanup operations.
'''
try:
    number = int(input("Enter e number: "))
    print("Number:", number)

except ValueError:
    print("Invalid input")
    
finally:
    print("Program execution finished.")
    
file = None
try:
    file = open(r"C:\Users\ADMIN\Documents\python-learning-zero-to-advance\12-Exception-Handling/students.txt", "r")
    content = file.read()
    print(content)
    
except FileNotFoundError:
    print("Student file not found.")

finally:
    if file is not None:
        file.close()
    
    print("File handling finished!")        
    
