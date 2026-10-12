# A parameter is the variable listed inside the parentheses in the function definition.
def greet(name): # parameter = name
    print("Hello", name)

# An argument is the actual value sent to the function when it is called.
greet("Atul") # argument = Atul
greet("Ankit")
greet("Anik")

# Two Parameters
def student_info(name, department):
    print("Name:", name)
    print("Department:", department)
    print(name)
    print(department)
student_info("Atul", "CIS")

def add(a, b):
    print(a + b)

add(10, 20)


# Three Parameters
def student(name, age, department):
    print("Name:", name)
    print("Age:", age)
    print("Department:", department)

student("Atul Paul", 21, "CIS")

# String Parameters
def welcome(name):
    print("Welcome", name)

welcome("Atul")

def square(number):
    print(number * number)
square(5)

def result(name, marks):
    print("Student:", name)
    print("Marks:", marks)

result("Atul", 90)
result("Anikt", 100)
