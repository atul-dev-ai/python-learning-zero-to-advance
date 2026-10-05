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