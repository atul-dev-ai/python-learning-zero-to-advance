'''
Argument na dile function nije theke default value use korbe.
'''
def greet(name):
    print("Hello", name)
greet("Atul Paul")

def default_arg(name = "Atul"):
    print("Hello", name)
default_arg()

# Default Value Override
default_arg("Ankit")

def welcome(name = "Student"):
    print("Welcome", name)
    
welcome()
welcome("Atul")

# Number Default value
def power(number, exponent = 2):
    return number ** exponent
print(power(5))
print(power(5, 3))

# Multiple Default Arguments
def student_info(name = "Unknown", age = 0):
    print("Name:", name)
    print("Age:", age)
student_info()
student_info("Atul", 21)

# Default + Normal Parameter
def greet(name, message = "Hello"):
    print(message, name)
greet("Atul")

# Default parameter er pore non-default parameter dewa jay na.


def student(name, department = "CIS"):
    print("Name:", name)
    print("Department:", department)
student("Atul")

# Default Argument + Return
def calculate_price(price, tax = 5):
    return price + (price * tax / 100)
result = calculate_price(1000, 10)
print(result)

def create_user(name, country = "Bangladesh"):
    print(name, country)
create_user("Atul")

# Task 1
def power(number, exponent = 3):
    return number ** exponent

print(power(5))
print(power(7, 4))

# Task 2
def student_infos(name, department = "Computing and Information System"):
    print(name)
    print(department)

student_infos("Atul")

# Task 3
def calculate_bill(amount, discount = 0):
    print(amount, discount)
calculate_bill(1000)
calculate_bill(10000, 400)

# Task 3