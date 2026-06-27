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

