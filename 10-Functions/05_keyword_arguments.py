'''
keyword argument er pore Positional Argument dewa jay na.
Duplicate value dile error.
'''

# Basic Example
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(name = "Atul Paul", age = 21)
student(name = "Ankit Paul", age = 9)

def student(name, age, dept = "CIS"):
    print(name)
    print(age)
    print(dept)
student(
    name = "Atul Paul",
    age = 21,
    dept = "CIS"
)
student(age = 22, name="Atul")

def calculate_bill(amount, discount = 0, tax = 5):
    final_price = amount - (amount * discount / 100)
    final_price = final_price + (final_price * tax / 100)
    
    return final_price

result = calculate_bill(
    amount= 1000,
    discount= 12,
    tax = 9
)
print(result)