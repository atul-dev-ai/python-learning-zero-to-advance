# default argument er value function define er somoy set kora hoy.

# Default argument holo function er parameter er value jodi function call er somoy na deya hoy tahole seta default value hishebe use hobe. 

# Function call korar somoy jodi 

def greet(name = "Coder"):
    print("Hello :", name)
greet("Atul")
greet()


def add (a, b):
    return a + b
print(add(1, 2))

def adds(a, b, c = 5):
    return a + b + c
print(adds(1, 2)) # a = 1, b = 2, c = 5(Default value)

print(adds(1, 2, 9)) # a = 1, b = 2, c = 9 (c er value function call er somoy deya hoyeche)

def square(number):
    return number * number
print(square(5))

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    elif num % 2 != 0:
        return "Odd"
    else:
        return "Invalid Input"
print(check_even_odd(5))

def check_admin(users = "Admin"):
    if users == "Admin":
        return "Welcome Admin"
    elif users == "User":
        return "Welcome User"
    else:
        return "Invalid User"
print(check_admin("Admin"))
print(check_admin("User"))
print(check_admin("Guest"))
print(check_admin()) # default value.

# finding maximum
def maximum(a, v):
    if a > v:
        return a
    else:
        return v
print(maximum(5, 10))


# student information 
def student_info(name, age, department = "CIS"):
    print("Name:", name)
    print("Age:", age)
    print("Department: ", department)
student_info("Atul", 21)
student_info("Atul", 21, "CIS major AI")

# calculating area of rectangle
def rectangle_area(length, width):
    return length * width
print("Area of rectangle: ", rectangle_area(5, 10))

# calculating simple interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
print("Simple Interest: ", simple_interest(1000, 5, 2))
print("Simple Interest 2: ", simple_interest(2000, 7, 4))