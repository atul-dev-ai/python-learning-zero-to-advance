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
