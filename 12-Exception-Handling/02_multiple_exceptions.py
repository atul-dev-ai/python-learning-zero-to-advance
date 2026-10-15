'''
Python checks the exception handlers and executes the first matching "except" block.
Once an exception occurs inside "try", the remaining statements in that "try" block are skipped.
'''
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("result:", result)

except ValueError:
    print("Please enter valid integers.")

except ZeroDivisionError:
    print("You cannot divide by zero.")