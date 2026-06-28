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


# multiplication table
def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}") # ekhane f-string use kora hoyche. f-string er maddhome variable ke string er moddhe use kora jay. ar ei f-string er moddhe variable ke {} er moddhe use kora hoyche. ei "X" holo multiplication er jonno use kora hoyche. ar ei "i" holo loop er variable.

multiplication_table(5)

# calculating total marks and percentage
def result(marks1, marks2, marks3):
    total = marks1 + marks2 + marks3
    percentage = (total / 300) * 100
    return total, percentage
total_marks, percentage = result(80, 95, 90)
print("Total marks: ", total_marks)
print("Percentage: ", percentage)