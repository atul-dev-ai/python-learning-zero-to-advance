'''
The "raise" keyboard allows you to explicitly trigger an exception when a condition 
in your program is not satisfied.
'''

age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative.")
# raise er por exception gotle seti samlanor upojokto except na thakle program ti error diye theme jabe.
print("Your age is:", age)

# raise and try-except
try:
    age = int(input("Enter your age: "))
    
    if age < 0:
        raise ValueError("Age cannot be negative.")
    
    print("Your age is:", age)
    
except ValueError as error:
    print("Error:", error)
    
    