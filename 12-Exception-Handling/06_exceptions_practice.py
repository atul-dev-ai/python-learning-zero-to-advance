class InvalidNumberError(Exception):
    pass

def divide_number():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if num1 < 0 or num2 < 0:
            raise InvalidNumberError(
                "Negative numbers are not allowed."
            )
        
        result = num1 / num2
        
    except ValueError:
        print("Error: Please enter valid numbers.") # like abs
        
    except ZeroDivisionError: # if zero
        print("Error: Cannot divide by zero.")
        
    except InvalidNumberError as error:
        print("Validation Error:", error)
        
    else:
        print("Result:", result)
        print("Calculation successful.")
        
    finally:
        print("Calculation attempt finished\n")
        
        
while True:
    print("=== Safe Calculator ===")
    print("1. Divide numbers")
    print("2. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        divide_number()
        
    elif choice == "2":
        print("Calculaator Closed.")
        break
    
    else:
        print("Invalid choice. Try again.\n")
        
        